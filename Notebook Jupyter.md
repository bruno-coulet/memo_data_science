

## Créer un notebook
 
- avec Jupyter :
	- ouvrir Anaconda
	- lancer Jupyter notebook
	- cliquer sur le bouton "new" et choisir un kernel
- avec un IDE : créer un fichier .ipynb

## Bases de données publiques
[kaggle](https://www.kaggle.com/)
https://data.gov/
https://www.data.gouv.fr/fr/
## [[IPython]]
interactive python, dépendance de Jupyter
interpréteur de commande ([[Shell]]) interactif, il fournit le kernel python
permet a l'OS de comprendre les commande
coloration syntaxique
complétion

## Jupyter
Julia Python R
Projet de développement de notebook, adaptation à d'autres langages (Julia et R)
Développe des outils et services pour faire de la programmation interactive
Utile pour la data science
Utilise le kernel iPython  pour interpréter python.
#### fonctions magiques `%` et `%%`
`%`  agit sur une ligne
`%%`    agit sur une cellule

les **magic commands** de Jupyter sont des commandes spéciales qui facilitent certaines tâches, comme la :
- gestion des modules
- le profilage du code
- l'interaction avec le système

- `%lsmagic` : Liste toutes les fonctions magiques disponibles.
- `%help` : Affiche l'aide d'une commande magique.
- `%timeit` : Mesure le temps moyen d'exécution d'une ligne (plusieurs itérations).
- `%%timeit` : Mesure le temps moyen d'exécution d'une cellule entière.
- `%matplotlib inline` : Affiche les graphiques de Matplotlib directement dans le notebook.
- `%reset` : Réinitialise l'espace de travail en supprimant toutes les variables.
- `%who` : Liste les variables définies dans l'espace de travail.
- `%pwd` : Affiche le répertoire de travail actuel.
- `%cd <path>` : Change le répertoire de travail.
- `%ls` : Liste les fichiers dans le répertoire courant.
- `%run <script.py>` : Exécute un script Python dans l'espace de travail actuel.
- `%load <script.py>` : Charge le contenu d'un fichier dans une cellule.
- `%%writefile <filename>` : Écrit le contenu de la cellule dans un fichier.

**`%time`** : Mesure le temps d'exécution d'une ligne de code.
```python
%timeit x = sum(range(1000))
```

**`%%time`** : Mesure le temps d'exécution de toute une cellule.
```python
%%timeit
x = sum(range(1000))
y = sum(range(2000))
```


## [[Anaconda]]
Distribution libre de Python et R la plus connue en data Science
contient de nombreuses librairies, jupyter Notebook, Rstudio, etc...

## Notebook
Document executable, peut être exporté en HTML, PDF, LaTeX
Enregistré sous le format .ipynb (pour IPythonNotebook)

Application web qui  permet de  :
- stocker et interpréter des lignes de code
- affiche le résultat de l’exécution du code (graphiques, tableaux, etc.)
- |affiche du texte formaté, figures, liens... 

Comparable à une page web contenant du code Python et markdown
Simplifie l'analyse de données.

**<font : color ='red'>Mode commande</font>** : par défaut
contour de la cellule selectionnée est bleu

Entrée ou clic sur une cellule -> passe en **<font : color ='red'>mode edition</font>**
contour de la cellule en vert
petit crayon à côté du kernel

Echape ou clic hors d'une cellule -> passe en **<font : color ='red'>Mode commande</font>**


Help / Keyboard shortcut 

### Mode commande
C'est le mode par défaut, le contour de la cellule sélectionnée est bleu

| Raccouci clavier      | effet                                                                                                                                  |                                             |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| `!`                   | permet d'exécuter des commandes système (comme dans un terminal ou une invite de commande) directement depuis une cellule du notebook. |                                             |
| **`A`**               | insère une cellule avant                                                                                                               |                                             |
| **`B`**               | insère une cellule après                                                                                                               |                                             |
| **``CTRL F``**        | chercher/remplacer                                                                                                                     |                                             |
| **`M`**               | transforme la cellule en markdown                                                                                                      |                                             |
| **`Y`**               | transforme la cellule en code                                                                                                          |                                             |
| double **`D`** rapide | supprime la cellule                                                                                                                    | z pour annnuler                             |
| **`Z`**               | retour en arrière                                                                                                                      |                                             |
| **``CTRL /``**        | commente le code                                                                                                                       |                                             |
| CTRL entrée           | exécuter la cellule                                                                                                                    | Le code est envoyer au kernel qui l'exécute |
| SHIFT entrée          | Execute la cellule et sélectionne la suivante                                                                                          |                                             |
| CTRL S                | enregistre les modifications                                                                                                           |                                             |
| Shift J               | sélectionne la cellule en dessous                                                                                                      |                                             |
| flêches haut/ bas     | Navigue d'une cellule à l'autre                                                                                                        |                                             |
|                       |                                                                                                                                        |                                             |

Mode Edition :

- `shift J`  selectionne la cellule dessous, peut être répété ad libidum
- `ctrl A`    sélectionne le contenu d'une cellule
- `tab`          Indente  le contenu d'une cellule
- `ctrl z`    retour en arrière
- `ctrl /`   commente le code
- `ctrl s`   enregistre