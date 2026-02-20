"""
ComfyUI-Pythza — Utility nodes for ComfyUI
https://github.com/Pythza/ComfyUI-Pythza
"""

WEB_DIRECTORY = "./js"


# ── Node Navigator ───────────────────────────────────────────────────────────

class PythzaNodeNavigator:
    """UI-only node with a button that pans the canvas to a target node by ID."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "node_id": ("INT", {"default": 0, "min": 0, "max": 99999}),
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "noop"
    CATEGORY = "Pythza"
    OUTPUT_NODE = True

    def noop(self, node_id):
        return {}


# ── Registration ─────────────────────────────────────────────────────────────

NODE_CLASS_MAPPINGS = {
    "PythzaNodeNavigator": PythzaNodeNavigator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PythzaNodeNavigator": "Node Navigator (Pythza)",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']
