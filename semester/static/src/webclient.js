odoo.define("semester.semesterService", [
    "web.core.browser",
    "web.core.network.rpc",
    "web.core.registry",
    "web.session",
    "web.orm_service",
    "web.core.browser.cookie",
    "web.core.user",
    "web.core.browser.router",
], function (require) {
    "use strict";

    const browser = require("web.core.browser");
    const { rpcBus } = require("web.core.network.rpc");
    const { registry } = require("web.core.registry");
    const session = require("web.session");
    const { UPDATE_METHODS } = require("web.orm_service");
    const { cookie } = require("web.core.browser.cookie");
    const { user } = require("web.core.user");
    const { router } = require("web.core.browser.router");

    const CIDS_SEPARATOR = "-";

    function parseSemesterIds(cids, separator = CIDS_SEPARATOR) {
        if (typeof cids === "string") {
            return cids.split(separator).map(Number);
        } else if (typeof cids === "number") {
            return [cids];
        }
        return [];
    }

    function computeActiveSemesterIds(cids) {
        const { user_semesters } = session;
        let activeSemesterIds = cids || [];
        const availableSemestersFromSession = user_semesters.allowed_semesters;
        const notAllowedSemesters = activeSemesterIds.filter(
            (id) => !(id in availableSemestersFromSession)
        );

        if (!activeSemesterIds.length || notAllowedSemesters.length) {
            activeSemesterIds = [user_semesters.current_semester];
        }
        return activeSemesterIds;
    }

    function getSemesterIds() {
        let cids;
        // backward compatibility, in old urls cid was still used.
        // deprecated as of saas-17.3
        const state = router.current;
        if ("cids" in state) {
            // backward compatibility s.t. old urls (still using "," as separator) keep working
            // deprecated as of 17.0
            if (typeof state.cids === "string" && !state.cids.includes(CIDS_SEPARATOR)) {
                cids = parseSemesterIds(state.cids, ",");
            } else {
                cids = parseSemesterIds(state.cids);
            }
        } else if (cookie.get("cids")) {
            cids = parseSemesterIds(cookie.get("cids"));
        }
        return cids || [];
    }

    const semesterService = {
        dependencies: ["action", "orm"],
        start(env, { action, orm }) {
            const allowedSemesters = session.user_semesters.allowed_semesters;
            const disallowedAncestorSemesters = session.user_semesters.disallowed_ancestor_semesters;
            const allowedSemestersWithAncestors = {
                ...allowedSemesters,
                ...disallowedAncestorSemesters,
            };
            const activeSemesterIds = computeActiveSemesterIds(getSemesterIds());

            // update browser data
            cookie.set("cids", activeSemesterIds.join(CIDS_SEPARATOR));
            user.updateContext({ allowed_semester_ids: activeSemesterIds });

            // reload the page if changes are being done to `res.semester`
            rpcBus.addEventListener("RPC:RESPONSE", (ev) => {
                const { data, error } = ev.detail;
                const { model, method } = data.params;
                if (!error && model === "res.semester" && UPDATE_METHODS.includes(method)) {
                    if (!browser.localStorage.getItem("running_tour")) {
                        action.doAction("reload_context");
                    }
                }
            });

            return {
                allowedSemesters,
                allowedSemestersWithAncestors,
                disallowedAncestorSemesters,

                get activeSemesterIds() {
                    return activeSemesterIds.slice();
                },

                get currentSemester() {
                    return allowedSemesters[activeSemesterIds[0]];
                },

                getSemester(semesterId) {
                    return allowedSemestersWithAncestors[semesterId];
                },

                /**
                 * @param {Array<>} semesterIds - List of semesters to log into
                 * @param {boolean} [includeChildSemesters=true] - If true, will also
                 * log into each child of each semesterIds (default is true)
                 */
                async setSemesters(semesterIds, includeChildSemesters = true) {
                    const newSemesterIds = semesterIds.length ? semesterIds : [activeSemesterIds[0]];

                    function addSemesters(semesterIds) {
                        for (const semesterId of semesterIds) {
                            if (!newSemesterIds.includes(semesterId)) {
                                newSemesterIds.push(semesterId);
                                addSemesters(allowedSemesters[semesterId].child_ids);
                            }
                        }
                    }

                    if (includeChildSemesters) {
                        addSemesters(
                            semesterIds.flatMap((semesterId) => allowedSemesters[semesterId].child_ids)
                        );
                    }

                    cookie.set("cids", newSemesterIds.join(CIDS_SEPARATOR));
                    user.updateContext({ allowed_semester_ids: newSemesterIds });

                    const controller = action.currentController;
                    const state = {};
                    const options = { reload: true };
                    if (controller?.props.resId && controller?.props.resModel) {
                        const hasReadRights = await user.checkAccessRight(
                            controller.props.resModel,
                            "read",
                            controller.props.resId
                        );

                        if (!hasReadRights) {
                            options.replace = true;
                            state.actionStack = router.current.actionStack.slice(0, -1);
                        }
                    }

                    router.pushState(state, options);
                },
            };
        },
    };

    registry.category("services").add("semester", semesterService);

    return semesterService;
});
