# ComfyUI-Pythza

A small utility node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI).

## 🧭 Node Navigator

Pan the canvas to any node by its ID. Useful for large workflows where you need to jump between distant nodes quickly.

- Enter a **node ID** and click **"Go to node"**
- The canvas centers on the target node instantly
- Works like a bookmark, but you choose the destination on the fly

> **Tip:** You can find a node's ID by right-clicking it in ComfyUI — it's shown at the top of the context menu.

## Installation

### Manual
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Pythza/ComfyUI-Pythza.git
```
Restart ComfyUI.

## Structure
```
ComfyUI-Pythza/
├── __init__.py       # Node definition (Python)
├── js/
│   └── pythza.js     # Frontend (canvas navigation)
└── README.md
```

## License
MIT
