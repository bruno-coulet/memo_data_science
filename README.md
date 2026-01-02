# Mémo Data Science

Ce dépôt contient :
- des notes Obsidian (`/obsidian`)
- des notebooks Jupyter générés automatiquement (`/notebooks`)
- des scripts utilitaires (`/scripts`)

Les notebooks sont générés à partir des fichiers Markdown.


🔴 Problème classique

Les notebooks génèrent :
- outputs volumineux
- diffs Git illisibles

🟢 Solution simple

Toujours nettoyer les outputs avant commit
`jupyter nbconvert --clear-output --inplace notebooks/*.ipynb`
ou sur mac
`python3 -m jupyter nbconvert --clear-output --inplace notebooks/*.ipynb`


👉 Versionne :
- le code
- le markdown
- pas les résultats

🟢 Solution automatique (pro)
Installer nbstripout

```python
pip install nbstripout
nbstripout --install
```


➡️ Les outputs sont automatiquement supprimés au commit

4️⃣ Workflow Git idéal (au quotidien)
# 1. Ecrire dans Obsidian
# 2. Génèrer les notebooks
`python scripts/md_to_ipynb.py`

# 3. (optionnel) Nettoyage outputs
`jupyter nbconvert --clear-output --inplace notebooks/*.ipynb`

# 4. Commit
```python
git add .
git commit -m "Ajout notes Obsidian + notebooks associés"
git push
```


