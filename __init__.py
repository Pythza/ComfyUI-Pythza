"""
ComfyUI-Pythza — Utility nodes for ComfyUI
https://github.com/Pythza/ComfyUI-Pythza
"""
import re

WEB_DIRECTORY = "./js"


# ── Helpers ───────────────────────────────────────────────────────────────────

STRIP_PREFIXES = ["SDXL_PONY_", "PONY_SDXL_", "SDXL_", "PONY_", "_SDXL_", "_PONY_"]
BLOCK_LABELS = ["Custom", "Slider", "Detail"]


def strip_prefix(name):
    for prefix in STRIP_PREFIXES:
        if name.upper().startswith(prefix.upper()):
            return name[len(prefix):]
    return name


def parse_lora(entry, label):
    entry = entry.strip()
    if not entry:
        return None
    match = re.match(r'<lora:([^>]+)>', entry)
    if not match:
        return None
    inner = match.group(1)
    parts = inner.rsplit(":", 1)
    if len(parts) != 2:
        return None
    path, strength = parts[0].strip(), parts[1].strip()
    filename = path.replace("\\", "/").split("/")[-1]
    filename = re.sub(r'\.safetensors$', '', filename, flags=re.IGNORECASE)
    clean = strip_prefix(filename)
    return f"{label}: {clean}\nStrength: {strength}"


def format_lora_string(lora_string):
    top_level = []
    depth = 0
    current = []
    for ch in lora_string:
        if ch == "<":
            depth += 1
        elif ch == ">":
            depth -= 1
        if ch == "," and depth == 0:
            top_level.append("".join(current).strip())
            current = []
        else:
            current.append(ch)
    top_level.append("".join(current).strip())

    lines = []
    for i, block in enumerate(top_level[:3]):
        label = BLOCK_LABELS[i] if i < len(BLOCK_LABELS) else f"Block{i+1}"
        parsed = parse_lora(block, label)
        if parsed:
            if lines:
                lines.append("")
            lines.append(parsed)

    return "\n".join(lines) if lines else "(no LoRAs)"


# ── Node 1: LoRA Formatter ───────────────────────────────────────────────────

class PythzaLoraFormatter:
    """Parses a LoRA tag string and displays a clean formatted preview."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "lora_string": ("STRING", {"forceInput": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("formatted",)
    FUNCTION = "format"
    CATEGORY = "Pythza"
    OUTPUT_NODE = True

    def format(self, lora_string):
        result = format_lora_string(lora_string)
        return {"ui": {"text": [result]}, "result": (result,)}


# ── Node 2: Count True Booleans ──────────────────────────────────────────────

class PythzaCountTrue:
    """Counts how many of the connected boolean inputs are True."""

    @classmethod
    def INPUT_TYPES(cls):
        optional = {f"bool_{i}": ("BOOLEAN", {"default": False}) for i in range(1, 21)}
        return {"required": {}, "optional": optional}

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("true_count",)
    FUNCTION = "count"
    CATEGORY = "Pythza"

    def count(self, **kwargs):
        return (sum(1 for v in kwargs.values() if v is True),)


# ── Node 3: Node Navigator ──────────────────────────────────────────────────

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
    "PythzaLoraFormatter":  PythzaLoraFormatter,
    "PythzaCountTrue":      PythzaCountTrue,
    "PythzaNodeNavigator":  PythzaNodeNavigator,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PythzaLoraFormatter":  "LoRA Formatter (Pythza)",
    "PythzaCountTrue":      "Count True Booleans (Pythza)",
    "PythzaNodeNavigator":  "Node Navigator (Pythza)",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']
