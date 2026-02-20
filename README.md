# ComfyUI-Pythza

A small collection of utility nodes for [ComfyUI](https://github.com/comfyanonymous/ComfyUI).

## Nodes

### 🧭 Node Navigator
Pan the canvas to any node by its ID. Useful for large workflows where you need to jump between distant nodes quickly.

- Enter a **node ID** and click **"Go to node"**
- The canvas centers on the target node instantly
- Works like a bookmark, but you choose the destination on the fly

> **Tip:** You can find a node's ID by right-clicking it in ComfyUI — it's shown at the top of the context menu.

### 🎨 LoRA Formatter
Parses a LoRA tag string (e.g. `<lora:folder/MyModel:0.8>`) and displays a clean, readable preview.

- Strips common prefixes like `SDXL_`, `PONY_`, etc.
- Shows up to 3 LoRA blocks with labels (Custom, Slider, Detail)
- Live preview widget on the node itself

### 🔢 Count True Booleans
Counts how many of the connected boolean inputs are `True`. Accepts up to 20 optional boolean inputs.

Handy for conditional logic — e.g. "run this branch only if at least 3 options are enabled."

## Installation

### Manual
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/YOUR_USERNAME/ComfyUI-Pythza.git
```
Restart ComfyUI.

### ComfyUI Manager
Search for **Pythza** in the ComfyUI Manager install menu (once registered).

## Structure
```
ComfyUI-Pythza/
├── __init__.py       # Node definitions (Python)
├── js/
│   └── pythza.js     # Frontend (canvas navigation + LoRA preview widget)
└── README.md
```

## License
MIT
