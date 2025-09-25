odoo.define("semester.SwitchSemesterMenu", [
    "web.core.registry",
    "semester.SwitchSemesterItem",
    "web.core.dropdown.dropdown",
    "web.core.dropdown.dropdown_group",
    "web.core.dropdown.dropdown_item",
    "owl",
    "web.core.commands.command_hook",
    "web.core.l10n.translation",
    "web.core.utils.arrays",
    "web.core.utils.hooks",
    "web.core.hotkeys.hotkey_hook",
    "web.core.dropdown.dropdown_hooks",
], function (require) {
    "use strict";

    const { registry } = require("web.core.registry");
    const { SwitchSemesterItem } = require("semester.SwitchSemesterItem");

    const { Dropdown } = require("web.core.dropdown.dropdown");
    const { DropdownGroup } = require("web.core.dropdown.dropdown_group");
    const { DropdownItem } = require("web.core.dropdown.dropdown_item");

    const owl = require("owl");
    const { Component, useChildSubEnv, useRef, useState } = owl;

    const { useCommand } = require("web.core.commands.command_hook");
    const { _t } = require("web.core.l10n.translation");
    const { symmetricalDifference } = require("web.core.utils.arrays");
    const { useChildRef, useService } = require("web.core.utils.hooks");
    const { useHotkey } = require("web.core.hotkeys.hotkey_hook");
    const { useDropdownState } = require("web.core.dropdown.dropdown_hooks");

    class SemesterSelector {
		constructor(semesterService, dropdownState) {
			this.semesterService = semesterService;
			this.dropdownState = dropdownState;
			this.selectedSemestersIds = semesterService.activeSemesterIds.slice();
		}

		get hasSelectionChanged() {
			return (
				symmetricalDifference(this.selectedSemestersIds, this.semesterService.activeSemesterIds)
					.length > 0
			);
		}

		isSemesterSelected(semesterId) {
			return this.selectedSemestersIds.includes(semesterId);
		}

		switchSemester(mode, semesterId) {
			if (mode === "toggle") {
				if (this.selectedSemestersIds.includes(semesterId)) {
					this._deselectSemester(semesterId);
				} else {
					this._selectSemester(semesterId);
				}
			} else if (mode === "loginto") {
				if (this._isSingleSemesterMode()) {
					this.selectedSemestersIds.splice(0, this.selectedSemestersIds.length);
				}
				this._selectSemester(semesterId, true);
				this.apply();

				this.dropdownState.close?.();
			}
		}

		apply() {
			this.semesterService.setSemesters(this.selectedSemestersIds, false);
		}

		reset() {
			this.selectedSemestersIds = this.semesterService.activeSemesterIds.slice();
		}

		selectAll() {
			if (this.selectedSemestersIds.length > 0) {
				this.selectedSemestersIds.splice(0, this.selectedSemestersIds.length);
			} else {
				const newIds = Object.values(this.semesterService.allowedSemesters).map((c) => c.id);
				this.selectedSemestersIds.splice(0, this.selectedSemestersIds.length, ...newIds);
			}
		}

		_selectSemester(semesterId, unshift = false) {
			if (!this.selectedSemestersIds.includes(semesterId)) {
				if (unshift) {
					this.selectedSemestersIds.unshift(semesterId);
				} else {
					this.selectedSemestersIds.push(semesterId);
				}
			} else if (unshift) {
				const index = this.selectedSemestersIds.findIndex((c) => c === semesterId);
				this.selectedSemestersIds.splice(index, 1);
				this.selectedSemestersIds.unshift(semesterId);
			}
			this._getBranches(semesterId).forEach((semesterId) => this._selectSemester(semesterId));
		}

		_deselectSemester(semesterId) {
			if (this.selectedSemestersIds.includes(semesterId)) {
				this.selectedSemestersIds.splice(this.selectedSemestersIds.indexOf(semesterId), 1);
				this._getBranches(semesterId).forEach((semesterId) => this._deselectSemester(semesterId));
			}
		}

		_getBranches(semesterId) {
			return this.semesterService.getSemester(semesterId).child_ids || [];
		}

		_isSingleSemesterMode() {
			if (this.selectedSemestersIds.length === 1) {
				return true;
			}

			const getActiveSemester = (semesterId) => {
				const isActive = this.selectedSemestersIds.includes(semesterId);
				return isActive ? this.semesterService.getSemester(semesterId) : null;
			};

			let rootSemester = undefined;
			for (const semesterId of this.selectedSemestersIds) {
				let semester = getActiveSemester(semesterId);

				// Find the root active parent of the semester
				while (getActiveSemester(semester.parent_id)) {
					semester = getActiveSemester(semester.parent_id);
				}

				if (rootSemester === undefined) {
					rootSemester = semester;
				} else if (rootSemester !== semester) {
					return false;
				}
			}

			// If some children or sub-children of the root semester
			// are not active, we are in multi-semester mode.
			if (rootSemester && rootSemester.child_ids) {
				const queue = [...rootSemester.child_ids];
				while (queue.length > 0) {
					const semester = getActiveSemester(queue.pop());
					if (semester && semester.child_ids) {
						queue.push(...semester.child_ids);
					} else if (!semester) {
						return false;
					}
				}
			}

			return true;
		}
    }

    class SwitchSemesterMenu extends Component {
		static template = "semester.SwitchSemesterMenu";
		static components = { Dropdown, DropdownItem, DropdownGroup, SwitchSemesterItem };
		static props = {};
		static SemesterSelector = SemesterSelector;

		setup() {
			this.dropdown = useDropdownState();
			this.semesterService = useService("semester");

			this.semesterSelector = useState(
				new this.constructor.SemesterSelector(this.semesterService, this.dropdown)
			);
			useChildSubEnv({ semesterSelector: this.semesterSelector });

			this.searchInputRef = useRef("inputRef");
			this.state = useState({});
			this.resetState();

			useHotkey("control+enter", () => this.confirm(), {
				bypassEditableProtection: true,
				isAvailable: () => this.semesterSelector.hasSelectionChanged,
			});

			useCommand(_t("Switch Semester"), () => this.dropdown.open(), { hotkey: "alt+shift+u" });

			this.containerRef = useChildRef();
			this.navigationOptions = {
				hotkeys: {
					space: (index, items) => {
						if (!items[index]) {
							return;
						}
						if (items[index].el.classList.contains("o_switch_semester_item")) {
							const semesterId = parseInt(items[index].el.dataset.semesterId);
							this.semesterSelector.switchSemester("toggle", semesterId);
						}
					},
					enter: (index, items) => {
						if (!items[index]) {
							return;
						}
						if (items[index].el.classList.contains("o_switch_semester_item")) {
							const semesterId = parseInt(items[index].el.dataset.semesterId);
							this.semesterSelector.switchSemester("loginto", semesterId);
							this.dropdown.close();
						} else {
							items[index].select();
						}
					},
				},
			};
		}

		get hasLotsOfSemesters() {
			return Object.values(this.semesterService.allowedSemestersWithAncestors).length > 9;
		}

		get semestersEntries() {
			const semesters = [];

			const addSemester = (semester, level = 0) => {
				if (this.matchSearch(semester.name)) {
					semesters.push({ semester, level });
				}

				if (semester.child_ids) {
					for (const semesterId of semester.child_ids) {
						addSemester(this.semesterService.getSemester(semesterId), level + 1);
					}
				}
			};

			Object.values(this.semesterService.allowedSemestersWithAncestors)
				.filter((c) => !c.parent_id)
				.sort((c1, c2) => c1.sequence - c2.sequence)
				.forEach((c) => addSemester(c));

			return semesters;
		}

		get selectAllClass() {
			if (
				this.semesterSelector.selectedSemestersIds.length >=
				Object.values(this.semesterService.allowedSemesters).length
			) {
				return "btn-link text-primary";
			} else {
				return "btn-link text-secondary";
			}
		}

		get selectAllIcon() {
			if (
				this.semesterSelector.selectedSemestersIds.length >=
				Object.values(this.semesterService.allowedSemesters).length
			) {
				return "fa-check-square text-primary";
			} else if (this.semesterSelector.selectedSemestersIds.length > 0) {
				return "fa-minus-square-o";
			} else {
				return "fa-square-o";
			}
		}

		resetState() {
			this.state.searchFilter = "";
			this.state.showFilter = this.hasLotsOfSemesters;
		}

		onSearch(ev) {
			this.state.searchFilter = ev.target.value;
			this.state.showFilter = true;
		}

		matchSearch(semesterName) {
			if (!this.state.searchFilter) {
				return true;
			}

			const name = semesterName.toLocaleLowerCase().replace(/\s/g, "");
			const filter = this.state.searchFilter.toLocaleLowerCase().replace(/\s/g, "");
			return name.includes(filter);
		}

		handleDropdownChange(isOpen) {
			if (isOpen) {
				if (this.searchInputRef.el) {
					this.searchInputRef.el.focus();
				}

				if (this.containerRef.el) {
					// Fixes the container width so it doesn't change when searching.
					const currentWidth = this.containerRef.el.getBoundingClientRect().width;
					this.containerRef.el.style.width = currentWidth + "px";
				}
			} else {
				this.resetState();
			}
		}

		confirm() {
			this.dropdown.close();
			this.semesterSelector.apply();
		}

		get isSingleSemester() {
			return Object.values(this.semesterService.allowedSemestersWithAncestors ?? {}).length === 1;
		}
	}

	const systrayItem = {
		Component: SwitchSemesterMenu,
	};

	registry.category("systray").add("SwitchSemesterMenu", systrayItem, { sequence: 3 });

	return {
		SemesterSelector,
		SwitchSemesterMenu,
		systrayItem,
	};
});
