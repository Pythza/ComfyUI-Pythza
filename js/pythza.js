import { app } from "../../scripts/app.js";

// ── Node Navigator ──────────────────────────────────────────────────────────
app.registerExtension({
    name: "Pythza.NodeNavigator",

    async beforeRegisterNodeDef(nodeType, nodeData) {
        if (nodeData.name !== "PythzaNodeNavigator") return;

        const origOnNodeCreated = nodeType.prototype.onNodeCreated;
        nodeType.prototype.onNodeCreated = function () {
            if (origOnNodeCreated) origOnNodeCreated.apply(this, arguments);

            this.addWidget("button", "Go to node", null, () => {
                const idWidget = this.widgets?.find(w => w.name === "node_id");
                if (!idWidget) return;

                const targetId = parseInt(idWidget.value);
                const target = app.graph._nodes_by_id?.[targetId] ??
                               app.graph._nodes?.find(n => n.id === targetId);

                if (!target) {
                    alert(`Node #${targetId} not found in this workflow.`);
                    return;
                }

                const canvas = app.canvas;
                const [x, y] = target.pos;
                const [w, h] = target.size;

                canvas.ds.offset[0] = -x - w / 2 + canvas.canvas.width  / (2 * canvas.ds.scale);
                canvas.ds.offset[1] = -y - h / 2 + canvas.canvas.height / (2 * canvas.ds.scale);
                canvas.setDirty(true, true);
            });
        };
    }
});

// ── LoRA Formatter ──────────────────────────────────────────────────────────
app.registerExtension({
    name: "Pythza.LoraFormatter",

    async beforeRegisterNodeDef(nodeType, nodeData) {
        if (nodeData.name !== "PythzaLoraFormatter") return;

        const origOnNodeCreated = nodeType.prototype.onNodeCreated;
        nodeType.prototype.onNodeCreated = function () {
            if (origOnNodeCreated) origOnNodeCreated.apply(this, arguments);

            const textWidget = this.addWidget("text", "preview", "", () => {}, {
                multiline: true,
                readonly: true,
            });
            textWidget.inputEl?.setAttribute("readonly", true);
            this._previewWidget = textWidget;
            this.setSize([300, 200]);
        };

        const origOnExecuted = nodeType.prototype.onExecuted;
        nodeType.prototype.onExecuted = function (message) {
            if (origOnExecuted) origOnExecuted.apply(this, arguments);
            if (message?.text?.[0] !== undefined && this._previewWidget) {
                this._previewWidget.value = message.text[0];
                const lines = message.text[0].split("\n").length;
                this.setSize([300, Math.max(120, 40 + lines * 20)]);
                this.setDirtyCanvas(true);
            }
        };
    }
});
