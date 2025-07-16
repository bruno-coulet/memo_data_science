[Doc numpy](https://docs.scipy.org/doc/numpy-1.13.0/reference/ufuncs.html)
https://jalammar.github.io/visual-numpy/

```python
import numpy as np
```
## Intro Numpy

NumPy ( Numerical Python)
Est une librairie [[Python]] dédiée au calcul scientifique.
Ecrit en C (entre 50 et 100 x  plus rapide que python)
Permet de manipuler et d’effectuer rapidement et simplement de nombreuses opérations mathématiques sur un tableau de données :
- fonctions de calcul très performantes
- structures de données très performantes (ndarrays)

Les tableaux peuvent être utilisés comme des vecteurs ou des matrices grâce à des fonctions de **NumPy** qui permettent de réaliser des calculs matriciels utilisés en algèbre.
- [`numpy.dot()`](https://courspython.com/tableaux-numpy.html#numpy-dot)
- [`numpy.linalg.det()`](https://courspython.com/tableaux-numpy.html#numpy-linalg-det)
- [`numpy.linalg.inv()`](https://courspython.com/tableaux-numpy.html#numpy-linalg-inv)
- [`numpy.linalg.eig()`](https://courspython.com/tableaux-numpy.html#numpy-linalg-eig)
- etc

tableau multidimensionnels ou matrices
matrice = tableau d'éléments, composante essentielle de l’**algèbre linéaire**

 ![[matrice.png]]
## N dimension array
### `np.array`
La fonction [`.array()`](https://courspython.com/apprendre-numpy.html#numpy-array) permet de créer des ndarray (tableau à N dimensions)
autant de dimensions que nécessaire
Contrairement à une liste, l'array est <font color='red'>obligatoirement monotype.</font>
Cela permet d'utiliser moins de mémoire et d'espace de stockage.

| dimensions | code                                 | résultat                                                                                |         |
| ---------- | ------------------------------------ | --------------------------------------------------------------------------------------- | ------- |
| 1          | `np.array([1, 2])`                   | `array([1, 2])`                                                                         | vecteur |
| 2          | `np.array([[1], [2]])`               | `array([[1], [2]])`                                                                     | matrice |
| 3          | `np.array([[[1], [2]], [[3], [4]]])` | `array([[[1], [2]], [[3], [4]]])`                                                       | cube    |
| n          | `np.zeros((2, 3, 4))`                | Un tableau 3D rempli de zéros<br>2 lignes<br>3 colonnes<br>4  éléments dans la 3ème dim |         |
Optimisé pour le stockage de grand jeu de données, la manipulation et le calcul vectorisé
jusqu'a 30 x plus rapide qu'avec un tableau classique.

- On peut sélectionner au sein d’un array
- possèdent de nombreuses méthodes permettant de les manipuler ou d'effectuer des opérations mathématiques.
- on peut définir le `dtype` et le `shape` ou laisser python inférer ces valeurs


`dtype` :
- int
- float
- bool
- complex : nombres décimaux complexes
- bytes
- str
- number : tout types de nombres
- [Types numpy](https://numpy.org/doc/stable/user/basics.types.html)


```python
# Syntaxe
mon_array = np.array([élément1, élément2, élément3])
autre_array = np.array([élément1, élément2, élément3], dtype = int)


# Crée une liste
revenus = [1800, 1500, 2200, 3000, 2172]
# Crée un array à partir de cette liste
revenus_array = np.array(revenus)
# afficher l'array
revenus_array
# afficher le type de donné contenu dans l'array
revenus_array.dtype
# >>> dtype('int32')
```

<font color='red'>Si dans la liste de départ il y a des données de types différents, NumPy essaiera de tous les convertir au type le plus général. </font>

Par exemple, si un tableau contient des entiers (  `int`  ) et des nombres décimaux (`float` ), tous ses éléments seront convertis en nombres décimaux (`float` )

Les types en NumPy seront toujours présentés via deux informations :
- le **type** ( `int`  ) ;
- la **précision** ( `32`  ).

Cette dernière correspond au nombre de bits sur lesquels sont codés les nombres.
`int32` : entre                      -2 147 483 648  et 2 147 483 647 bits
`int64` : entre  -9 223 372 036 854 775 808 et 9 223 372 036 854 775 808


| `axis`   | Direction                       | Cela veut dire                                                           |
| -------- | ------------------------------- | ------------------------------------------------------------------------ |
| `axis=0` | vertical (de haut en bas)       | **On opère sur les lignes**, on applique l'opération colonne par colonne |
| `axis=1` | horizontal (de gauche à droite) | **On opère sur les colonnes**, on applique l'opération ligne par ligne   |

```python
x = np.array([1, 2, 3, 4])
x.shape
```
`>>> (4,)` → un vecteur ligne 

La méthode `.reshape(-1, 1)` sert à **changer la forme d’un tableau (array)**
Lorsqu’on a besoin de transformer un vecteur en **matrice colonne** :
```python
x.reshape(-1, 1)
x.shape
```
`>>>  (4, 1)` → une matrice colonne
```python
>>>array([[1],
          [2],
          [3],
          [4]])
```


### `.reshape(-1,1)`

`array.reshape(-1, 1)` transforme un tableau 1D en un tableau 2D à une seule colonne :

-  `-1`  : laisse NumPy deviner automatiquement combien de lignes il faut
-  `1`  :  une seule colonne
```python
a = np.array([10, 20, 30])
a.shape         # (3,)    tableau 1D

b = a.reshape(-1, 1)
b.shape         # (3, 1)  tableau 2D, 3 lignes, 1 colonne
```


### `array` avec des listes
Il est possible de créer un tableau 2D ou plus en utilisant une liste de listes au moyen de crochets imbriqués. Les listes internes correspondent à des lignes du tableau.

```python
tableau_1d = np.array([1,2,3])
```

```python
tableau_2d = np.array([[1, 2, 3], [4, 5, 6]])
```
Une liste de lignes
Les lignes contenues dans cette liste représentent les colonnes.
Ainsi chaque ligne contient une liste qui correspond aux colonnes de cette ligne

```python
np.array([
[ligne1_colonne1, ligne1_colonne2, ligne1_colonne3],
[ligne2_colonne1, ligne2_colonne2, ligne2_colonne3],
[ligne3_colonne1, ligne3_colonne2, ligne3_colonne3],
[ligne4_colonne1, ligne4_colonne2, ligne4_colonne3]
])
```

### `array` avec des fonctions numpy

- `np.ones(n)` : array de n éléments, rempli de 1

- `np.zeros(n)`:  array de n éléments, rempli de 0

- `np.eye(n)` : matrice identité (2 dimensions, des 1 sur la diagonale, des 0 ailleurs)

- `np.arange(i, j, p)`  : array rempli avec une séquence linéaire, qui ira de  i  à  j, par pas de  p

- `np.linspace(start, stop, x)` : array de  `x`  valeurs  uniformément espacées entre  `start`   et  `stop`

```python
# 3 lignes sur 5 colonnes rempli de 1
np.ones((3, 5))

# 4 lignes et 4 colonnes contenant que des 0
np.zeros((4, 4))

# un tableau de 6x3 rempli de valeurs aléatoires comprises entre 0 et 1
np.random.random((6, 3))

# un tableau de 3x3 rempli de valeurs aléatoires entières, comprises entre 1 et 10
np.random.randint(1, 10, size=(3, 3))
```
### Génération de nombre aléatoires
[Génération de nombre aléatoires](https://www.python-simple.com/python-numpy/random-numpy.php)
Module standard python et numpy[[random]]


 `[0.0, 1.0)` :

- La borne **0.0 est incluse**, donc les valeurs générées peuvent être égales à 0.0.
- La borne **1.0 est exclue**, donc les valeurs générées seront toujours strictement inférieures à 1.0, mais jamais égales à 1.0.      

| **Fonction**                            | **Génère pseudo-aléatoirement :**                                                                                                                                                                                     |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `np.random.random(size)`                | Des `float` uniformément distribués dans l'intervalle `[0.0, 1.0)`                                                                                                                                                    |
| `np.random.randint(low, high, size)`    | Des `int` aléatoires dans l'intervalle `[low, high)` avec une taille ou un shape spécifié                                                                                                                             |
| `np.random.randn(dims)`                 | Des nombres suivant une distribution normale centrée réduite :<br>- Moyenne `mean` $\mu$ = 0<br>- Écart-type `std` σ = 1<br>- Les valeurs possibles vont de −∞ à +∞<br>- 99.7 % comprises entre -3 et +3              |
| `np.random.choice(a, size, replace, p)` | Sélectionne aléatoirement des éléments d'une liste ou d'un tableau 1D.<br>- `a` : population à choisir<br>- `size` : nombre d'éléments<br>- `replace` : tirage avec ou sans remise<br>- `p` : probabilités associées. |
| `np.random.random_sample(size)`         | Des `float` uniformément distribués dans `[0.0, 1.0)` pour une taille donnée.                                                                                                                                         |



```python
np.random.randint(1, 10, 450)
```

- **1** : borne inférieure (inclus).
- **10** : borne supérieure (exclus).
- **450** : taille (ou shape) du tableau.

```python
np.random.randn(10)
```

- Génère 10 nombres aléatoires suivant une **distribution normale centrée réduite**.

```python
np.random.randn(10, 10)
```

- Génère un tableau 2D `10x10` contenant des nombres suivant une distribution normale centrée réduite.
- [[Maths#loi gaussienne / distribution gaussienne]]


```python
np.random.random_sample(7)
```

- Génère un tableau 1D de 7 nombres flottants dans `[0.0, 1.0)`.


**Pour des distributions spécifiques** :

Normale ( gausienne )
    `np.random.normal(mean, std, size)`
Binomiale : 
    `np.random.binomial(n, p, size)`
Poisson : 
    `np.random.poisson(lam, size)`


### Génération de nombre aléatoire avec une graine

2 possibilités :
- `np.random.seed` (peut avoir un impact sur d'autre calculs)
- créer un objet avec `np.RandomState` (plus propre)

```python
# objet avec une graine
rand_gen = np.random.RandomState(seed=12345)
# autre objet avec la même graine
rand_gen_2 = np.random.RandomState(seed=12345)

# Génère 2 chiffres (ou plus) avec ces objets
rand_gen.randn(2)
rand_gen_2.randn(2)
# Les 2 objets donnent le même résultat :
array([-0.20470766,  0.47894334]
array([-0.20470766,  0.47894334]
```

### Array à partir d'un fichier

Fonction `genfromtext()`   ( c'est celle qui à le plus d'option )

```python
mon_array = np.genfromtxt("mon-fichier.txt", delimiter=";", skip-header="true")
```
- fichier source
- délimiteur de colonnes
- ignore le header du fichier (optionnel)


**Enregistre l'array dans un fichier**
```python
np.savetxt("mon_array_enregistré.txt", mon_array, delimiter=";")
```
- fichier destination
- nom de la variable qui contient le ndarray
- délimiteur de colonnes



## NaN

Not A Number, valeur manquante

### `np.sum()`
- **Comporte les `NaN` dans le calcul.**
- Si le tableau contient un seul `NaN`, **le résultat sera aussi `NaN`**, car une opération avec `NaN` donne `NaN`
### `np.nansum()`
- **Ignore les `NaN`** dans le calcul.
- Très utile pour faire des statistiques sur des données incomplètes (par exemple des moyennes ou des totaux partiels)
```python
a = np.array([1, 2, np.nan])
np.sum(a)  # Résultat : nan
np.nansum(a)  # Résultat : 3.0
np.mean(a)  # Résultat : nan
np.nanmean(a)  # Résultat : 1.5
```
### `np.mean()`
- Calcule la **moyenne arithmétique**.
- Si le tableau contient un `NaN`, **le résultat sera `NaN`** (comme avec `np.sum()`)

### `np.nanmean()`
- Calcule la moyenne **en ignorant les `NaN`**
- Utile pour des jeux de données incomplets

| Fonction       | Résultat si `NaN` présent | Utilisation principale                |
| -------------- | ------------------------- | ------------------------------------- |
| `np.sum()`     | `NaN`                     | Calculs classiques, données complètes |
| `np.nansum()`  | somme sans le(s) `NaN`    | Données avec valeurs manquantes       |
| `np.mean()`    | `NaN`                     | Données complètes uniquement          |
| `np.nanmean()` | Moyenne sans le(s)`NaN`   | Données avec valeurs manquantes       |
| ...            |                           |                                       |

Si `np.sum(arr)`, `np.mean(arr)` ou `np.max(arr)` **ne retourne pas `NaN`** :
- alors il n'y a pas de `NaN` dans `arr
- sinon ces fonctions renverraient directement `NaN`

Contrairement à NumPy, [[Pandas#Valeur manquante : `NaN` vs. `NA`|pandas.DataFrame.sum()]] ignore les NaN par défaut
	comme `np.nansum()`

## Indexation

### Indexation simple

#### Accès à un élément spécifique d’un array  :   `nom_array[indice]` 

```python
# pour accéder au 5ème élement
mon_array[4] 
# pour accéder au dernier élément
mon_array[-1]
# On peut aussi modifier les valeurs par assignation
mon_array[1] = 1900
```

```python
# array à 2 dimensions, 3ème ligne, 2ème colonne :
mon_array[2,1]
```

#### Accès à certains éléments spécifiques via une condition :  `nom_array[condition]`  

### Indexation bolléenne

Garde uniquement les valeur du tableau qui sont supérieures à 10
```python
mon_array[mon_array > 10]
```
La condition `mon_array>10` génère un tableau de mêm dimension contenant uniqueent des valeurs booléenes.
Python ne garde que les valeur 'True'

il est possible de sélectionner des éléments selon une condition :

`nom_array[condition de sélection]`

L’array dans lequel on sélectionne, et la condition à appliquer, sont deux choses différentes. Même si cela concerne le même array, il est nécessaire de le spécifier également dans la condition !
Le résultat de ce qui est à l’intérieur des crochets doit forcément être un array ou une liste de booléens

```python
nom_array[nom_array > 2000]
# array([2200, 3000, 2172])
revenus_array[(revenus_array > 2000) & (revenus_array < 3000)]
# array([2200, 2172])

# Remplace tous les éléments supérieurs à 2 000 de l'array par 0.
revenus_array[revenus_array > 2000] = 0
```
& = et
 |  = ou
 Chaque condition doit être délimitée par des ()


### Fancy indexing

Sélectionner plusieurs éléments non consécutif de l'array via un tableau (ou une liste) d'indices entre crochets :

```python
# génère un tableau à une dimension
mon_array[ [18,7,9,2] ]
```

Permet également de structurer la sortie comme on le souhaite
On peut créer un array à plusieurs dimension à partir d'un array à une dimension :

```python
# génère un tableau à 2 dimensions
array_indices = np.array( [ [4,10,5], [12,9,8] ] )
mon_array[array_indices]
```

On obtient un tableau à 2 dimensions
3 colonnes et 2 lignes
lignes 1 avec les valeurs de mon_array  aux indices 4, 10 et 5
lignes 2 avec les valeurs de mon_array  aux indices 12, 9 et 8


## Slicing : 
```python
nom_array[début:fin:pas]
```

Accès à plusieurs éléments par tranche

indice du début,  facultatif si égal à `0`
indice de fin, facultatif si égal à `-1` ( ou `len(liste) )
pas, facultatif si égal à `1`

| SLICING |          | par défaut         |
| ------- | -------- | ------------------ |
| début   | inclusif | 0 (début de liste) |
| fin     | inclusif | -1 (fin de liste)  |
| pas     |          | 1                  |

```python
nom_array[début:fin:pas]

# Les 3 premiers éléments
nom_array[:3]

# Tous les éléments à partir de l’indice 2
nom_array[2:]

# Un élément sur deux
nom_array[::2]

# Pas négatif, le début et la fin du slice sont inversés,ça inverse le tableau
nom_array[::-1]

# tout l'array
mon_array[:]
```

### Slicing à 2 dimensions:
`nom_array[début:fin:pas, début:fin:pas]`

A gauche la slice des lignes
A droite la slice des colonnes
```python
# Affiche les 2 premières lignes et les 4 premières colonnes :
mon-array[:2,:4]
# lignes index 0 et 1
# colonnes index 0, 1, 2 et 3


# Affiche les lignes à partir de 146 et les colonnes à partir de 3 :
mon-array[145:,2:]
```








## Vue & copie
- #### Vue
<font color='red'>Attention !</font>
Lorsqu'on fait du slicing sur un tableau, on crée une vue (comme un zoom) et pas une copie du tableau.
<font color='red'>Une modification du sous tableau entraine une modification du tableau initial</font>
Une copie prend 2x plus de temps qu'une vue, et de la mémoire suplémentaire.

- #### Copie
Méthode `copy()`
```python
mon_array = [1,2,3,4,5,6,7,8,9,10]
# Crée un sous tableau en copie qui prend les 5 premières valeurs
sous_tableau = mon_array[:5].copy()
# On peut modifier sous_tableau sans modifier mon_array
sous_tableau[0] = 50

```



## Opérations arithmétiques

Toutes les opérations se font élément par élément
A la différence des listes :

| Opération         | Résultat               |
| ----------------- | ---------------------- |
| `list_1 + list_2` | colle les deux listes  |
| `arr_1 + arr_2`   | addition terme à terme |

Fonctions:
- `add()
- `subtract()
-  `multiply()
- `divide()
```python
# Additionne l'ensemble des éléments d'un tableau avec un nombre
np.add(mon_array, 10)
# Additionne 2 tableau
np.add(mon_array,autre_array)
# Multiplie l'ensemble des éléments d'un tableau avec le nombre 10
np.multiply(mon_array, 10)
```

Avec des tableaux de dimensions différentes (Broadcasting) :

**Broadcasting** :  gère des calculs vectoriel sur des array de tailles variées
Cela est possible si les 2 dimensions sont égales ou si l'une des 2 dimension  est égale à 1 

```python
tableau_1 = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
tableau_2 = np.array([1, 5, 9])

tableau_3 = np.subtract(tableau_1, tableau_2)
			''' Enleve 1 à chaque valeur de la première colonne
					   5 à chaque valeur de la deuxième colonne
					   9 à chaque valeur de la troisième colonne
				'''
print(tableau_3)
>>>
[[ 9  6  3]
 [12  9  6]
 [15 12  9]]
```

Avec des tableaux de mêmes dimensions :

Chaque valeur du tableau 1 est multipliée/additionnée/soustraite/...  par la valeur à la même position de l'autre tableau.

## Agrégation
Permettent d'explorer un tableau :

| calcule la moyenne                      | ``.mean()``               |                         |
| --------------------------------------- | ------------------------- | ----------------------- |
| calcule la médiane                      | ``.median()``             |                         |
| le maximum                              | ``.max()``                |                         |
| le minimum                              | ``.min()``                |                         |
| accéder à l’indice de l’élement minimum | ``.argmin()``             |                         |
| accéder à l’indice de l’élement maximum | ``.argmax()``             |                         |
| calcule la somme                        | ``.sum()``                |                         |
| somme cumulative                        | ``.cumsum()``             |                         |
| coéfficient de corrélation              | ``.corrcoef()``           |                         |
| écart type                              | ``.std()``                |                         |
Peut être appliqué soit à l'ensemble des éléments soit par colonne, soit par ligne.

```python
# somme sur tout le tableau, retourne une seule valeur
np.sum(moon_array)
# retourne une valeur par colonne
np.sum(moon_array, axis=0)
# retourne une valeur par ligne
np.sum(moon_array, axis=1)
```

```python
# Ajout de la nouvelle ligne
new_row = [1900, 31, 1]
mon_array = np.vstack((mon_array, new_row))
```

## Tri

| ordonner par ordre croissant            | ``.sort()``               | array 1d                |
| --------------------------------------- | ------------------------- | ----------------------- |
| ordonner par ordre décroissant          | ``array[::-1].sort()``    | array 1d                |
| ordonner sur une colonne                | `arr[arr[:,1].argsort()]` | tri sur la 2ème colonne |

[Liste de l’ensemble des méthodes applicables à un array](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html)

## Attributs d'inspection
Les objets de classes ndarray possèdent un ensemble d'[attributs](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html) qui permettent de les inspecter

attributs : variable liée à une classe d'objet
permet d'accèder aux informations d'un objet via la syntaxe :
```python
objet.attribut
```

| ``mon_array.dtype`` | type des éléments                                      |
| ------------------- | ------------------------------------------------------ |
| ``mon_array.size``  | nombre des éléments                                    |
| ``mon_array.T``     | Fait la transposé, (inversion ligne/colonnes)          |
| ``mon_array.ndim``  | dimensions                                             |
| ``mon_array.shape`` | taille des dimension (nombre de lignes et de colonnes) |
## Ajouter / supprimer des éléments
### Ajouter des éléments

| fonction `append()` | ajoute à la fin du tableau |
| ------------------- | -------------------------- |
| fonction `insert()` | ajoute à l'index donné     |

```python
np.append(mon_array,        element_à_ajouter)
np.insert(mon_array, index, element_à_ajouter)
```

**array à 1 dimension :**
```python
# ajoute 5 valeurs à la fin du tableau
np.append(mon_array,    [1, 2, 3, 4, 5])
np.insert(mon_array, 1, [1, 2, 3, 4, 5])
```

**array à 2 dimensions :**
préciser sur quel axe on ajoute les valeurs
double crochet pour donner un tableau à 2 dimension en entrée à append
Il faut respecter la structure, 5 valeurs s'il y 5 colonnes, etc...
```python
# ajoute une ligne de 5 valeurs a la fin du tableau, double [[]]
np.append(mon_array, [[1, 2, 3, 4, 5]], axis=0)
# ajoute une ligne a l'index 1
np.insert(mon_array, 1, [1, 2, 3, 4, 5], axis=0)
```

Si on ne précise pas l'axe, NumPy transforme le tableau 2d en tableau à une dimension.

### Supprimer des éléments
```python
np.delete(mon_array, index, axe)
```
Si on ne précise pas l'axe, les élements aux index donnés seront supprimés.
Si on précise un axe, les colonnes/lignes aux index donnés seront supprimés.


## Diviser un tableau

| split()  | tableau 1 dimension                    |
| -------- | -------------------------------------- |
| hsplit() | diviser horizontalement un tableau 2 d |
| vsplt()  | diviser verticalement un tableau 2 d   |
```python
np.split(mon_array,index)
# sur les tableaux à 2 dimensions :
np.hsplit(mon_array,index)
np.vsplit(mon_array,index)
```
**array à 1 dimension :**
```python
# découpe en 3 tableaux, de 0 à 1, de 2 à 5, de 6 à -1
np.split (mon_array, [2,6])
```
**array à 2 dimensions :**
```python
# coupe verticalement en 2 tableaux
# lignes 0 à 1, lignes 2 à -1
np.vplit (mon_array, [2])
```

```python
# coupe horizontalement
# colonnes  0 et 1 dans le tableaux 1, les autres dans le tableau 2
np.hplit (mon_array, [2])
```

## Concaténer / combiner les tableaux

| concatenate() |     |
| ------------- | --- |
| vstack()      |     |
| hstack()      |     |
**array à 1 dimension :**
```python
np.concatenate([mon_array_1,mon_array_2])
```
**array à 2 dimensions :**
si l'ion respecte la même structure (nombre de colonnes) on peut concaténer plusieurs tableaux 2d.

## Empiler des tableaux de dimensions différentes

array_1 à 1 dimension   : [40,50,60]

array_2 à 2 dimensions : [ [1,2,3], 
                    [4,5,6]
					[7,8,9] ]
	
```python
array_1 = np.array([40,50,60])
array_2 = np.array([ [1,2,3],  [4,5,6], [7,8,9] ], dtype="float")

# empilement vertical, il faut le même nombre de colonnes
np.vstack([array_1,mon_array_2])

>>> [[40. 50. 60.]
>>>  [1. 2. 3.]
>>>  [4. 5. 6.]
>>>  [7. 8. 9.]]

# empilement horizontal, il faut le même nombre de lignes -> on redéfini array_1
array_1 = np.array([[40],[50],[60]])
np.hstack([array_1,mon_array_2])

>>> [[40. 1. 2. 3.]
>>>  [50. 4. 5. 6.]
>>>  [60. 7. 8. 9.]]


```




## Matrices 

### `mat` ( OBSOLETE )
Le type `mat` permet de préciser que le tableau est une matrice.
Cela permet de faire des opérations matricielles :
- multiplication  par un scalaire
- produit matriciel
- transposition
- etc...
- 
fonction `mat()`
```python
ma_matrice = np.mat (mon_array)
```


### numpy.array()
création de matrices à partir d’une liste .

```python
matrice = np.array([[ 1, 2, 3],[ 4, 5, 6]])
```
### numpy.matrix()
Syntaxe :
`numpy.matrix(input,dtype)   `

paramètres :
- **Input :** les éléments d’entrée pour former une matrice.
- **Dtype :** le type de données correspondant à la sortie.

```python
# Setting the data-type to int
matriceB = np.matrix('[1,2;3,4]', dtype=np.int32) 
```

### numpy.arrange()
```python
print(numpy.array([numpy.arange(1,5), numpy.arange(5,10)]))  
print('\nMatriceB:\n', matriceB)
```  


Attribut  : 

| `T` | Transposée            | ( comme les tableau ) |
| --- | --------------------- | --------------------- |
| `H` | Transposée conjuguée  |                       |
| `I` | Inverse de la matrice |                       |
```python
ma_matrice.T

# produit de la matrice par elle même (ma_matrice * ma_matrice)
ma_matrice**2
```


## Calculs

Si `ma_matrice` est un array (pas une matrice) :
`ma_matrice**2`  donne un array avec tous les éléments puissance 2.

### Produit matriciel

entre 2 array (tableau) A et C
```python
produit_matriciel = np.dot(A, C)
# ou
produit_matriciel = A @ C
```

- Méthode `dot()` permet de le faire sans avoir à les transformer en objet `mat`
- L’opérateur `@`  n’est disponible que depuis Python 3.5

[Manipulation d'array](https://numpy.org/doc/stable/reference/routines.array-manipulation.html)


### Produit scalaire

multiplication de chaque valeur de l'array/vecteur un par la valeur du même index de l'array/vecteur 2, puis additionne le tout

en dimension 3, si les deux vecteurs x→![{\displaystyle {\vec {x}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/db2dc6ced9cc3bc7e8b9f2707cbec033f6d3759c) et y→![{\displaystyle {\vec {y}}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/5f0c914c24b65c8c8b48ddbc6acbc092d5458c4b) ont pour coordonnées respectives (_x_1, _x_2, _x_3) et (_y_1, _y_2, _y_3), on obtient alors la formule :

x→⋅y→=x1y1+x2y2+x3y3![{\displaystyle {\vec {x}}\cdot {\vec {y}}=x_{1}y_{1}+x_{2}y_{2}+x_{3}y_{3}}](https://wikimedia.org/api/rest_v1/media/math/render/svg/99eb066fb4cd2c19e9219e7eb62b20f3411d724f).

 