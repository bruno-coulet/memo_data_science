"""
scripts.md_to_ipynb

OBJECTIF : convertit les fichiers markdown en notebook Jupyter

UTILISATION :
cd scripts
python md_to_ipynb.py

"""


from pathlib import Path
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

OBSIDIAN_DIR = Path("../obsidian")
NOTEBOOK_DIR = Path("../notebooks")

NOTEBOOK_DIR.mkdir(exist_ok=True)

def md_to_ipynb(md_path, ipynb_path):
    with md_path.open(encoding="utf-8") as f:
        lines = f.read().splitlines()

    cells = []
    buffer = []
    in_code = False

    for line in lines:
        if line.strip().startswith("```python"):
            if buffer:
                cells.append(new_markdown_cell("\n".join(buffer)))
                buffer = []
            in_code = True
            continue

        if line.strip() == "```" and in_code:
            cells.append(new_code_cell("\n".join(buffer)))
            buffer = []
            in_code = False
            continue

        buffer.append(line)

    if buffer:
        cell = new_code_cell if in_code else new_markdown_cell
        cells.append(cell("\n".join(buffer)))

    nb = new_notebook(cells=cells)

    with ipynb_path.open("w", encoding="utf-8") as f:
        nbformat.write(nb, f)

def convert_all():
    for md_file in OBSIDIAN_DIR.glob("*.md"):
        ipynb_file = NOTEBOOK_DIR / (md_file.stem + ".ipynb")
        md_to_ipynb(md_file, ipynb_file)
        print(f"✔ {md_file.name} → {ipynb_file.name}")

if __name__ == "__main__":
    convert_all()
