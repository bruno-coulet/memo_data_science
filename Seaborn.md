[Documentation et tutoriels Seaborn](https://seaborn.pydata.org/api.html) 
[[Matplotlib]]

```python
import seaborn as sns
```

## Intro
Librairie qui permet de générer des graphiques à partir de [[Pandas]]
Reprend les mêmes principes que [[Matplotlib]] 
Ajoute des qualités de graphiques différents, de nouvelles fonctionnalités “par-dessus”.

-  Seaborn est une surcouche de Matplotlib ; il est donc possible de mixer des fonctions des deux librairies sur un seul et même graphique.

- Seaborn est né pour faciliter la création de visualisations à partir des data frames Pandas. Grâce à cette philosophie, on peut ajouter autant de dimensions (couleur, forme, taille, etc.) que de variables dans un data frame.

- Seaborn ajoute une dimension esthétique à ses graphiques, en donnant la possibilité de changer les thèmes et/ou les palettes de couleurs avec de multiples modèles graphiques prédéfinis.

Il est possible d’utiliser l’ensemble des options de personnalisation de [[Matplotlib]] directement sur des graphiques tracés avec Seaborn.
Les deux librairies se complètent pour exploiter au mieux les avantages de l’une et de l’autre

## Fonctions

| Fonctions                                                                                                            |                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `lineplot`                                                                                                           | trace des courbes                                                                                                         |
| `boxplot`                                                                                                            | boîte à moustache                                                                                                         |
| `histplot`                                                                                                           | histogrammes                                                                                                              |
| `kdeplot`                                                                                                            | graphique à densité                                                                                                       |
| `pairplot`                                                                                                           | tracer l’ensemble des variables numériques deux à deux, sur un seul graphique                                             |
| `set_palette` par exemple :<br>`sns.set_palette('pastel')`<br>`sns.set_palette('dark')`<br>`sns.set_palette('Set2')` | fixe une nouvelle palette<br>[Documentation palettes de couleur](https://seaborn.pydata.org/tutorial/color_palettes.html) |
| `set_theme`  par exemple :<br>`sns.set_theme()`<br>                                                                  | Applique un theme prédéfini.<br>Un ensemble d'aspects graphiques sur les axes, le fond, la graduation, etc.<br>           |
| `sns.set_theme(style='whitegrid', palette='pastel')`                                                                 | Mixe le choix du thème et une palette de couleurs                                                                         |
| `countplot`                                                                                                          |                                                                                                                           |

### Fonction `scatterplot`

| arguments | définit le                                                             |           |
| --------- | ---------------------------------------------------------------------- | --------- |
| `data`    | data frame qui va être utilisé pour tracer le graphique                |           |
| `x`       | variables du data frame à mettre en abscisse                           |           |
| `y`       | variables du data frame à mettre en ordonnée                           |           |
| `hue`     | colorise les données<br>crée une couleur pour chaque valeur existante. | optionnel |
| `size`    | associant la taille d’un point à lune valeur existante                 |           |

```python
sns.scatterplot(data=prets, x='revenu', y='taux_endettement', hue='type')
```

```python
# définit pour tous les graphiques la taille de la police de tous les éléments (xlabel, title, legend, etc.) à 14.
plt.rcParams.update({'font.size': 14})
# limites des graduations des absices de 500 à 7 500
plt.xlim(500, 7500)
# Affiche le grille
plt.grid()
# La fonction legend affiche le grapique
# l’argument`bbox_to_anchor` fixe la position de la légende en dehors du graphique, aux coordonnées (1,1)
plt.legend(bbox_to_anchor=(1, 1))

plt.show)()
```

## Agrégez des données avec Seaborn

La fonction`barplot`  permet d'agréger des données directement à l’intérieur du graphique
```python
sns.barplot(data=prets, x='ville', y='remboursement', errorbar=None, estimator=sum)
```

| arguments   |            | définit le                                                              |
| ----------- | ---------- | ----------------------------------------------------------------------- |
| `errorbar`  | `=None`    | confidence interval, ajoute les intervalles de confiance à chaque barre |
| `estimator` | `=sum`<br> | fonction d’agrégation                                                   |
|             |            |                                                                         |
