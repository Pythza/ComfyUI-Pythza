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
