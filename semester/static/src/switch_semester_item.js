odoo.define("semester.SwitchSemesterItem", [
    "web.core.dropdown.dropdown_item",
    "owl",
    "web.core.utils.hooks",
], function (require) {
    "use strict";

    const { DropdownItem } = require("web.core.dropdown.dropdown_item");
    const owl = require("owl");
    const { Component, useState } = owl;
    const { useService } = require("web.core.utils.hooks");

    class SwitchSemesterItem extends Component {
        static template = "semester.SwitchSemesterItem";
        static components = { DropdownItem, SwitchSemesterItem };
        static props = {
            semester: {},
            level: { type: Number },
        };

        setup() {
            this.semesterService = useService("semester");
            this.semesterSelector = useState(this.env.semesterSelector);
        }

        get isSemesterSelected() {
            return this.semesterSelector.isSemesterSelected(this.props.semester.id);
        }

        get isSemesterAllowed() {
            return this.props.semester.id in this.semesterService.allowedSemesters;
        }

        get isCurrent() {
            return this.props.semester.id === this.semesterService.currentSemester.id;
        }

        logIntoSemester() {
            if (this.isSemesterAllowed) {
                this.semesterSelector.switchSemester("loginto", this.props.semester.id);
            }
        }

        toggleSemester() {
            if (this.isSemesterAllowed) {
                this.semesterSelector.switchSemester("toggle", this.props.semester.id);
            }
        }
    }

    return SwitchSemesterItem;
});
