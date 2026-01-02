"""
scripts/md_to_ipynb.py

OBJECTIF : convertit un fichier markdown en notebook Jupyter

UTILISATION :
cd scripts
python md_to_ipynb.py chemin/vers/fichier.md
"""

import sys
from pathlib import Path
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell


# 📍 Chemin absolu vers le dossier du script
SCRIPT_DIR = Path(__file__).resolve().parent
NOTEBOOK_DIR = SCRIPT_DIR.parent / "notebooks"
NOTEBOOK_DIR.mkdir(exist_ok=True)


def md_to_ipynb(md_path: Path, ipynb_path: Path):
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


def main():
    if len(sys.argv) != 2:
        print("❌ Usage : python md_to_ipynb.py chemin/vers/fichier.md")
        sys.exit(1)

    md_file = Path(sys.argv[1])

    if not md_file.exists() or md_file.suffix != ".md":
        print("❌ Le fichier fourni doit être un fichier Markdown existant (.md)")
        sys.exit(1)

    ipynb_file = NOTEBOOK_DIR / (md_file.stem + ".ipynb")

    md_to_ipynb(md_file, ipynb_file)
    print(f"✔ {md_file.name} → {ipynb_file.name}")


if __name__ == "__main__":
    main()
