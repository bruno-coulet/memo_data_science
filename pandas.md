retranscription des livres :
- Python pour la data science, éditions ENI, page 198
- [Python pour le data scientist](https://github.com/bruno-coulet/pythondatascientist), éditions Dunod
## intro
Importer la librairie :
 ```python
import pandas as pd
```

| ligne   | <font color="orange">individus</font>  ou <font color="orange">observation</font><br> |
| ------- | ------------------------------------------------------------------------------------- |
| colonne | <font color="orange">variables</font> ou <font color="orange">champs</font>           |
  **Librairie** python qui s'appuie sur [[Numpy]] et apporte 2 structures essentielles pour l'analyse de données :

| Structures de donnée :  |                                                                                                                                                                                       |                           |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| [DataFrame](#DataFrame) | peut être assimilé à un tableau 2 dimensions<br>est constitué d'autant de `Series` qu'il a de colonnes                                                                                | par défaut                |
|                         | - structure sous forme de tableau<br>- chaque colonne à des éléments de même type<br>- indexé par des ``index`` pour les lignes<br>- indexé par des ``columns`` pour les colonnes<br> |                           |
| [Series](#Series)       | peut être assimilé à un vecteur<br>suite de valeurs stockées dans une colonne et indexées<br>                                                                                         | option `squeeze=True`<br> |
|                         |                                                                                                                                                                                       |                           |
- un ensemble de méthodes et de fonctions associées pour
	- explorer les dataframes et series
	- les nettoyer 
	- les transformer 
	- les manipuler
	- les visualiser
- permet de stocker des données de types différents (un par série / colonne)
- possibilité d'assigner une étiquette aux données plutôt qu'un index numérique
- manipule efficacement les données manquantes
- manipule efficacement les données de série temporelles (time series data)
- lit les données provenant de différentes sources, des fichiers délimités (CSV ou texte), ou encore des fichiers JSON ou Excel.
---
---
## Types

Il faut un seul type par colonne

### 3 types principaux :
- entiers  :      `Int8`, `Int16`, `Int32`, `Int64`. Peut gérer des valeurs manquantes (`NaN`)
- décimaux :   `float32` ou `float64`
- autres types : `object`

### types courants dans Pandas :

| Type        | Exemple Pandas                    | Description                          |
| ----------- | --------------------------------- | ------------------------------------ |
| `int`       | `Int8`, `Int16`, `Int32`, `Int64` | Nombres entiers (avec ou sans `NaN`) |
| `float`     | `float64`                         | Nombres réels                        |
| `bool`      | `boolean`                         | Booléens (avec ou sans `NaN`)        |
| `object`    | `object`                          | Chaînes de caractères ou objets      |
| `string`    | `string`                          | Chaînes de caractères (natif)        |
| `datetime`  | `datetime64[ns]`                  | Dates et heures                      |
| `timedelta` | `timedelta64[ns]`                 | Durées                               |
| `category`  | `category`                        | Données catégoriques                 |
| `period`    | `Period`                          | Périodes de temps                    |
| `interval`  | `Interval`                        | Intervalles                          |

Ces types permettent une manipulation efficace des données selon leur nature et leur structure.

|                              | Python  | Pandas          |
| ---------------------------- | ------- | --------------- |
| Chaines de caractères, texte | `str`   | `object`        |
| Valeurs entières numériques  | `int`   | `int32`/`int64` |
| Valeurs réelles à virgule    | `float` | `float64`       |
| booléens True ou False       | `bool`  | `bool`          |
| ...                          |         |                 |

```python
# Vérifier les types du dataframe
print(df.dtypes)
```
---
## Importer/export

Pour Forcer PAndas à afficher toutes les colonnes
```python
pd.set_option('display.max_columns', None)
```


### Lecture de fichier texte ou excel 

| options        | spécifie le séparateur                         |
| -------------- | ---------------------------------------------- |
| `sep = ,`      | <font color='orange'>par défaut</font> virgule |
| `sep = \t`     | tabulation  (tab-separated values, SAP, Excel) |
| `sep = r’\s+’` | plusieurs espaces                              |
| `sep = ;`      | point virgule                                  |

| options        |                                                                 |
| -------------- | --------------------------------------------------------------- |
| `columns =`    | une liste des colonnes qu'on souhaite exporter                  |
| `Index = `     | `True`par défaut : écrit les labels/index des lignes            |
| `sheet_name =` | si on veut un autre onglet que le 1er du fichier excel          |

#### option `header`

<font color='orange'>Par défaut, python prend la 1ère ligne du fichier comme header</font>

Si le fichier source ne contient pas de header
On peut le spécifier afin que python ne le crée pas :
```python
nom_dataframe = pd.read_csv('nom_du_fichier.csv', header = None)
```
Les noms de colonne seront 0,1,2,3,etc...
Si le fichier source à un header, il sera considéré comme la 1ère ligne du tableau, cela peut générer des erreurs de type (`int` au lieu de `str` par exemple).



#### option `names`
Pandas ne prend pas le header du fichier et en crée un avec les noms de colonnes en argument :
```python
nom_dataframe = pd.read_csv('nom_du_fichier.csv', names = ['colonne_1', 'colonne_2'] )
```

#### option `skiprows`
Permet d'ignorer certaines lignes lors de la lecture du fichier et ne les stocke pas dans le tableau :
```python
nom_dataframe = pd.read_csv('nom_du_fichier.csv', skiprows=1, header = None)
```


#### option `index_col`
Spécifie quelle colonne du dataset correspond à l'index
il est possible d'avoir plusieurs index :
```python
nom_dataframe = pd.read_csv('nom_du_fichier.csv', index_col = 0 )
# ou
nom_dataframe = pd.read_csv('nom_du_fichier.csv', index_col = [0,5] )
```

#### option `squeeze`
Crée un `Serie` au lieu d'un `DataFrame` (par défaut)
```python
pd.read_csv("fichier.csv", squeeze=True)
```

#### option `usecols`
Si toutes les colonnes ne nous intéressent pas, on peut les filtrer 
```python
# filtrer avec les positions des colonnes
pd.read_csv("fichier.csv", usecols=[3,6])
# filtrer avec les noms des colonnes
pd.read_csv("fichier.csv", usecols=[colonne_nom, colonne_age])
```

#### option `dtype`
Spécifier le type des colonnes avec un dictionnaire

| clé               | valeurs               |
| ----------------- | --------------------- |
| noms des colonnes | `dtype` de la colonne |

```python
pd.read_csv("fichier.csv", dtype{"colonne_1":"Int64", "colonne_2":"float64", "colonne_3":"object"})
```
---

#### 📅 Gestion des dates : bonnes pratiques
Parser = analyser la syntaxe d'un texte

l'argument `parse_dates` indique quelles colonnes du fichier CSV doivent être interprétées comme des dates.
Converti automatiquement des colonnes contenant des dates en objets **datetime**
##### 1. Charger un fichier CSV avec une colonne de dates comme index

```python
# La colonne 'Date' devient l'index du DataFrame
# Pandas convertit automatiquement cette colonne en datetime
df = pd.read_csv(    "fichier.csv",index_col="Date", parse_dates=True)
```

* `index_col="Date"` est idéal pour des séries temporelles.
* `parse_dates=True` dit à Pandas de détecter les dates dans l'index.
* Le type obtenu est : `datetime64[ns]`.


##### 2. Convertir une colonne spécifique en datetime lors du chargement

```python
# Convertit la 5ème colonne (index 4) en datetime64[ns]
df = pd.read_csv("fichier.csv", parse_dates=[4])
```

* `parse_dates=[4]` permet de convertir uniquement certaines colonnes.
* Utile si le fichier a plusieurs colonnes date et que tu veux garder le contrôle.
* Évite les mauvaises interprétations si certaines colonnes ressemblent à des dates sans en être !


##### 3. Convertir une colonne en datetime après chargement
 `format` permet de forcer un format de date (FR / international)
```python
df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
```

###### Bonnes pratiques :

* Toujours utiliser `pd.to_datetime()` plutôt que `astype("datetime")`.
* Gère beaucoup plus de formats automatiquement, et détecte les erreurs.
* Si le fichier est français (`31/12/2023`), Pandas peut se tromper.
* `format` rend la conversion **plus rapide** et **plus fiable**.


##### 4. Gérer les erreurs de parsing proprement

```python
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
```

###### Effet :

* Les dates invalides deviennent `NaT` (équivalent de NaN pour les dates).
* Très utile pour nettoyer des fichiers Excel ou CSV mal formés.


##### 5. Extraire des informations temporelles utiles

```python
df["Année"] = df["Date"].dt.year
df["Mois"] = df["Date"].dt.month
df["Jour"] = df["Date"].dt.day
df["Semaine"] = df["Date"].dt.isocalendar().week
df["Jour_sem"] = df["Date"].dt.day_name()   # Monday, Tuesday…
```


##### 6. Trier par date (toujours nécessaire)

```python
df = df.sort_values("Date")
```

Indispensable avant :

* des graphiques temporels
* du resampling
* des calculs glissants (rolling)


##### 7. Résampling (très utile en time-series)

```python
df.resample("M").mean()   # données mensuelles
df.resample("W").sum()    # données hebdomadaires
df.resample("D").ffill()  # remplissage avant
```

##### 8. Identifier les fréquences temporelles

```python
pd.infer_freq(df.index)
```

Retourne `"D"`, `"M"`, `"H"`, etc.
✔ Très utile pour vérifier que l’index est uniforme.


🔹 la gestion desFuseaux horaires (`tz_localize`, `tz_convert`)
🔹 les dates irrégulières
🔹 les time deltas (`Timedelta`)

---

#### option `sheet_name`
Pour importer une autre feuille que la 1ère du fichier excel
```python
# avec les positions des colonnes
pd.read_csv("fichier.csv", sheet_name="nom_de_la_feuille")
```

###  Importation depuis une base de donnée
exemple avec une bdd SQLite avec la fonction `read_sql`:

```python
import sqlite3
connexion = sqlite3.connect('../chemin/bdd.db')
requete = "SELECT * FROM nom_table;"
resultats = pd.read_sql(requete, con=connexion)
resultats.head()
```

### Lecture de fichier au format `.json`
format texte pour l'échange de données de manière structurée et légère

```python
pd.read_json("../datasets/employees.json")
```



### Ecriture de fichier ou exportation de données
```python
mon_dataframe.to_csv("mes_resultats.csv")
```

| options      |                                                            |
| ------------ | ---------------------------------------------------------- |
| `sep`        | pour spécifier le séparateur, par défaut c'est la virgule. |
| `columns`    | une liste des colonnes qu'on souhaite exporter             |
| `header`     | écrire un en tête (par défaut)                             |
| `Index`      | `True`par défaut : écrit les labels/index des lignes       |
| `sheet_name` | Défini le nom de la feuille (onglet)                       |

```python
mon_dataframe.to_csv("mes_resultats.csv", sep=";")
mon_dataframe.to_csv("mes_resultats.csv", columns=["colonne_1", "colonne_5"])
```

---
---
## Valeur manquante : `NaN` vs. `NA`


- **NaN** (`Not a Number`) de **NumPy** : valeur flottante limité aux **données numériques**.
- **NA** (`Not Available`) de **Pandas**: pour les **types non numériques** (textes, catégories, etc.).


Pandas recommande d’utiliser **`pd.NA`** pour une meilleure gestion des données manquantes :<br>
**`pd.NA`** est plus flexible et fonctionne avec les types Pandas (`Int64`, `String`, `Boolean`).
  

| Caractéristique                       | `NaN` (`numpy.nan`)                        | `NA` (`pd.NA`)                                                     |
| ------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------ |
| **Type**                              | `float`                                    | `pandas._libs.missing.NAType` (nullable)                           |
| **Utilisation principale**            | Données numériques                         | Données avec types *nullable* : `Int64`, `boolean`, `string`, etc. |
| **Comportement logique**              | `np.nan != np.nan`                         | `pd.NA == pd.NA` → renvoie **`pd.NA`** (indéterminé)               |
| **Comparaison (`==`)**                | Toujours `False` (même `np.nan == np.nan`) | Renvoie `pd.NA`, pas `True`                                        |
| **Opérations mathématiques**          | OK → résultat : `nan`                      | Souvent **erreur** (`TypeError`)                                   |
| **Support des dtypes nullable**       | ❌ Non                                      | ✅Oui                         |
| **Détecté par `isna()` / `isnull()`** | ✅Oui                                     | ✅ Oui                          |
| **Fonctionne avec `fillna()`**        | ✅                                        | ✅ Oui                          |
| **Effet sur les dtypes**              | Force les colonnes en `float`              | Garde le type nullable d’origine (`Int64`, `boolean`, `string`)    |
| **Compatibilité booléens**            | Problématique                              | Compatible avec `BooleanDtype()`                                   |
| **Types de données typiques**         | Floats                                     | Nullable Pandas types                                              |


<br>
➡️ Pour la data science classique : np.nan suffit<br>
➡️ Pour garder des colonnes int ou bool avec NA : utiliser pd.NA

Contrairement à **Numpy**, **`pandas.DataFrame.sum()` ignore les `NaN`par défaut** :<br>
calcule la somme en ignorant les `NaN`comme `np.nansum()`

### Machine learning `NaN`✅, `Na`❌ 
Les bibliothèques ML attendent presque toutes des `NaN` :
- scikit-learn
- XGBoost
- LightGBM
- CatBoost
- TensorFlow / Keras
- PyTorch
-statsmodels

Toutes s’attendent explicitement à recevoir des `floats` et des `np.nan` pour représenter les valeurs manquantes<br>
`pd.NA` n’est pas reconnu dans la majorité des modèles.



#### `NaN` (`numpy.nan`)

- `Not a Number`
	utilisé principalement pour représenter des valeurs numériques manquantes.
- **Type** : `float`
- **Provenance** : `numpy.nan`


| NaN                           | Not a Number                                         |
| ----------------------------- | ---------------------------------------------------- |
| `NaN != NaN`                  | Deux `NaN` ne sont **jamais égaux** entre eux        |
| `type(np.nan)`                | `float`                                              |
| `pd.isna(x)`<br>`np.isnan(x)` | Teste si une valeur est un `NaN`                     |
| `np.nansum()`                 | somme de tous les éléments en **ignorant** les `NaN` |



```python
df = pd.DataFrame({"A": [1, 2, np.nan, 4]})

         A
    0  1.0
    1  2.0
    2  NaN
    3  4.0
```

#### NA (`pd.NA`)

- `Not Available` : Valeur manquante générique, introduite dans Pandas 1.0 pour gérer à la fois les types numériques et non numériques.<br>
**données non numériques** ou **catégorielles** ou **`object`**, `str`
- **Type** : `pd.NA` (au lieu de `float`)
- **Provenance** : Pandas (`pd.NA`)
- **Meilleure compatibilité** avec les `Int64`, `String`, et `Boolean`
- fait partie du type `pd.NA`, pour gérer de manière uniforme les valeurs manquantes.
  
   
```python
df = pd.DataFrame({"A": [1, 2, pd.NA, 4]})

         A
    0    1
    1    2
    2  <NA>
    3    4
```

	
### Gestion des `NaN` et `NA`

Pandas a été conçu pour que ces fonctions traitent tous les types de valeurs manquantes :
- `np.nan` (float NaN)
- `None`
- `pd.NA` (nouveau système NA de pandas)
- `pd.NaT` (date manquante)

→ Toutes sont détectées par `isna()` / `isnull()` et gérées par `fillna()` et `dropna()`

Vérifier la présence de valeurs manquantes

```python
df.isna()  # Identique à df.isnull()
df.isna().any()      # False ou True, colonne par colonne
df.isna().any().any() # True si au moins un NaN quelque part
```

Remplacer les valeurs manquantes

```python
df.fillna(0)  # Remplace NaN ou NA par 0
```

`fillna` remplace tous les NaN par :

```python
# 0
df.fillna(0)
# la dernière valeur connue (forward fill)
df.fillna(method='ffill')
# la prochaine valeur connue (backward fill)
df.fillna(method='bfill')
# la moyenne de chaque colonne
df.fillna(df.mean())
```

DataFrame de 3 colonnes, 4 lignes, avec des valeurs manquantes :
```python
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 2, 3, np.nan],
    'C': [1, np.nan, np.nan, 4]
})
```

	Original        ->        ffill            ->        bfill

| A   | B   | C   |     | A   | B   | C   |     | A   | B   | C   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |     |
| 1   | NaN | 1   | ->  | 1   | Nan | 1   | ->  | 1   | 2   | 1   |
| 2   | 2   | NaN |     | 2   | 2   | 1   |     | 2   | 2   | 4   |
| NaN | 3   | NaN |     | 2   | 3   | 1   |     | 4   | 3   | 4   |
| 4   | NaN | 4   |     | 4   | 3   |     |     | 4   | NaN | 4   |

Supprimer les lignes contenant des valeurs manquantes

```python
df.dropna()

# supprime les lignes où la colonne `"ma_colonne"` contient des NaN
df.dropna(subset=["ma_colonne"])

```
---










---

## Methodes

| Méthode           | `Series` | `DataFrame` |
| ----------------- | -------- | ----------- |
| `.sort_values()`  | ✅        | ✅           |
| `.loc`            | ✅        | ✅           |
| `.iloc`           | ✅        | ✅           |
| `.groupby()`      | ❌        | ✅           |
| `.drop()`         | ❌        | ✅           |
| `del`             | ❌        | ✅           |
| `.pop()`          | ❌        | ✅           |
| `.rename()`       | ❌        | ✅           |
| `.astype()`       | ✅        | ✅           |
| `pd.to_numeric()` | ✅        | ✅           |
| `.nunique()`      | ✅        | ✅           |
| `.reset_index()`  | ❌        | ✅           |
| `.pivot_table()`  | ❌        | ✅           |
| `pd.concat()`     | ❌        | ✅           |
| `.merge()`        | ❌        | ✅           |
| `.join()`         | ❌        | ✅           |
|                   |          |             |


### Méthodes des objets de classes `Series`
[Doc](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)

| méthodes pour les séries |                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `describe()`             | affiche un résumé statistique sur les valeurs de la série :<br>`count`  nombre sans compter les valeurs manquante<br>`mean`    moyenne <br>`std`      déviation standard écart type<br>`min`      valeur minimum<br>`25%`      quartiles ,divise le données en 4 parts égales<br>`50%`      des individus font moins que la valeur<br>`75%`      des individus font moins que la valeur<br>`max`      valeur maximum |
| `value_count()`          | visualise les valeurs uniques et leurs nombre                                                                                                                                                                                                                                                                                                                                                                        |
| `replace()`              | remplace une ou +ieurs valeurs par une autre                                                                                                                                                                                                                                                                                                                                                                         |
| `set_index()`            | redéfini les index                                                                                                                                                                                                                                                                                                                                                                                                   |

### Ajouter  des valeurs

La méthode `pd.concat()` permet de concaténer des `Series` ou des `DataFrame`.  
On peut concaténer plusieurs objets de même type (`Series` avec `Series`, ou `DataFrame` avec `DataFrame`).  
Cela permet d'ajouter des lignes ou des colonnes selon l'axe spécifié.

Par sécurité, `pd.concat()` retourne une copie (un nouvel objet) et n'applique pas le traitement sur l'objet original.

On peut lui assigner le même nom pour forcer le changement de l'original :

#### Pour une `Series` :

```python
ma_serie = pd.concat([ma_serie, pd.Series([liste_valeurs], index=["liste de label"])])
```

#### Pour un `DataFrame` :

```python
mon_dataframe = pd.concat([mon_dataframe, pd.DataFrame([[liste_valeurs]], columns=["colonne1", "colonne2"])], ignore_index=True)
```

- Pour concaténer des `Series` ou des `DataFrame`, `pd.concat()` peut être utilisé pour ajouter des lignes (par défaut) ou des colonnes, selon l'argument `axis`.
- Par défaut, `axis=0` ajoute des lignes, et `axis=1` ajoute des colonnes.

Cela couvre les deux cas d'usage !


### Supprimer une valeur

La méthode `drop()` permet de supprimer des éléments (lignes ou colonnes) en fonction de leur étiquette d'index spécifiée en option.

#### Pour une `Series` :

```python
ma_serie.drop(labels=["index_1", "index_2"], inplace=False)
```

#### Pour un `DataFrame` :

```python
mon_dataframe.drop(labels=["index_1", "index_2"], axis=0, inplace=False)  # Supprimer des lignes
# ou
mon_dataframe.drop(labels=["colonne1", "colonne2"], axis=1, inplace=False)  # Supprimer des colonnes
```

| `inplace=False`  | La modification est effectuée sur une copie        | Par défaut |
| ---------------- | -------------------------------------------------- | ---------- |
| `inplace=True`   | La modification est effectuée sur l'objet original |            |

#### Remarque :

- La méthode `drop()` modifie l'objet en place uniquement si `inplace=True` est spécifié.
- Sur une `Series`, cela supprimera des éléments selon leur étiquette d'index.
- Sur un `DataFrame`, cela supprime des lignes (`axis=0`, par défaut) ou des colonnes (`axis=1`).

### Modifier les valeurs

Les indexeurs `loc` et `iloc` sont utilisés pour modifier des valeurs dans une `Series` ou un `DataFrame`.

#### Avec `loc` (pour une `Series` ou un `DataFrame`), on sélectionne par étiquette d'index :

```python
ma_serie.loc["nom_index"] = nouvelle_valeur
# ou pour modifier plusieurs valeurs :
ma_serie.loc["nom_index_1", "nom_index_2"] = [nouvelle_valeur_1, nouvelle_valeur_2]
```

#### Avec `iloc` (pour une `Series` ou un `DataFrame`), on sélectionne par position d'index :

```python
ma_serie.iloc[position] = nouvelle_valeur
```

- **`loc`** : Lorsque plusieurs éléments ont la même étiquette d'index dans une `Series` ou un `DataFrame`, toutes les occurrences seront modifiées.
- **`iloc`** : Chaque position est unique, donc **seule l'occurrence à la position donnée sera modifiée**.

#### Exemple avec une `Series` :

```python
# Modifier la valeur à l'index 'nom_index'
ma_serie.loc["nom_index"] = "nouvelle_valeur"

# Modifier la valeur dans une `Series` avec un autre index
ma_serie.iloc[2] = "nouvelle_valeur_position_2"
```

#### Exemple avec un `DataFrame` :

```python
# Modifier une cellule en utilisant `loc`
mon_dataframe.loc[3, "nom_colonne"] = "nouvelle_valeur"

# Modifier plusieurs cellules
mon_dataframe.loc[2, ["colonne1", "colonne2"]] = ["valeur1", "valeur2"]
```

Les indexeurs permettent de manipuler les données de manière flexible selon les besoins de sélection et de modification.


---
## `Serie`
objet, structure de donnée

colonne du data frame,
tableau à 1 dimension (vecteur),
suite de valeurs représentant une variable pour un ensemble d'observation/individu

possède :
- un nom
- des <font color='orange'>index</font> `index`par défaut des `ìnt` à partir de 0, incrémente de 1
  peut être remplacer par des <font color='orange'>étiquettes</font> du type que l'on souhaite
- des valeurs `values()`
- un seul axe, l'axe des index

Accès aux valeurs de la série :
- avec la \[ position de la valeur \]
- avec l'\[ étiquette \]


[ensemble des méthodes et attributs des Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)

### Créer une `Serie`

Le stockage de valeurs de types hétérogènes est permis mais il est fortement conseillé de n'utilisé qu'<font color='orange'>un seul type de donnée</font>.

- méthode `Series()`
  à partir d'une liste, d'un tableauNumPy, d'un distionnaire
- fonctions de lecture de fichier `read_table()`, `read_csv()
    ```python
  ma_serie=pd.Series(donnees)
  
  ma_serie_2=pd.read_table('chemin_du_fichier.txt')
```

#### à partir de valeurs aléatoires
Avec `choice` du module `random` de NumPy :
```python
# syntaxe
pd.Series(np.random.choice(data, size))
# exemple pour 10 valeurs entre 0 et 500 (exclu)
pd.Series(np.random.choice(list(range(0,500)), 10))
```
`dtype: int32` ou `int64`
#### à partir d'une liste
Attention car <font color='orange'>les listes acceptent des données hétérogène, ce n'est pas conseillé</font>
La serie aura alors le `dtype: object` qui correspond au `str` et aux types mixtes
```python
# syntaxe
ma_serie=pd.Series(numpy_array)
```

#### à partir d'un tableau Numpy (ndarray)
```python
# syntaxe
pd.Series(liste)
# exemple avec 10 valeurs entre 0 et 499
ma_serie=pd.Series([2,5,7,'T',False])
```

#### à partir d'un fichier texte
```python
# avec la colonne 5 seulement
ma_serie=pd.read_csv('mon_fichier.csv', usecols=[5], squeeze=True)
```
#### Choisir l'index d'une série
```python
# avec les colonnes 5 et 7, la colonne 5 sert d'index
ma_serie=pd.read_csv('mon_fichier.csv', usecols=[5,7], index_col=[5], squeeze=True)
```


Affiche le type d'une colonne (variable) avec la fonction `type`:
```python
type(nom_dataframe[nom_variable])
```

### Accéder aux valeurs d'une `Serie`

Indexing : vouloir  accéder à un sous ensemble de notre structure
#### Indexing via la position des valeurs

```python
# Accéder à la position 2
ma_serie[1]
# Accéder aux positions 2, 8 et 13
ma_serie[[1,7,12]]
# Accéder à la dernière valeur
ma_serie[-1]
```

#### Indexing via l'étiquette des valeurs

```python
# Accéder à la valeur dont l'étiquette est le string 'patates'
ma_serie["patates"]
# Accéder a plusieurs valeurs 
ma_serie[["patates","carottes","concombres"]]
# Accéder à la dernière valeur
ma_serie[-1]
```


#### Indexeurs loc et iloc

Si les étiquettes sont des entier (comme les positions), Pandas ne saura pas ce que l'on cherche.

```python
# effectue l'indexing sur les étiquettes
ma_serie.loc[etiquette]
# effectue l'indexing sur les position 
ma_serie.iloc[position]

```


#### Indexing via une expression booléenne

Se base sur les valeurs et pas sur les positions.

```python
ma_serie[ma_serie>10]

ma_serie[ (ma_serie>10) & (ma_serie<30) ]
```
1. crée une nouvelle série de la même taille , contenant des valeurs booléennes
2. récupère l'ensemble des valeurs `True`

Effectuer plusieurs opérations booléennes avec les opérateurs bitwise :

| [[Opérateurs bitwise]] |          | touche Mac  |
| ---------------------- | -------- | ----------- |
| `&`                    | et       |             |
| \|                     | ou       |             |
| ~                      | négation | `alt` + `N` |

Les opérateurs logiques fonctionnent bien sur des expressions qui renvoient une valeur unique, avec les `Serie`ils renvoient une erreur



#### Slicing : découpage de valeurs successive

[Voir le slicing avec Python](Python.md#SLICING)  stop non inclus

Récupère un sous ensemble de données
Sélectionne les valeurs et les index.
N'utilise que les positions, pas les étiquettes (génère une erreur)

```python
# Avec les crochets
ma_serie[start:stop:step]
# Avec iloc - Conseillé
ma_serie.iloc[start:stop:step]

# Toutes les valeurs de la série sauf les 2 dernières
ma_serie.iloc[:-2]
# Seulement les 2 dernières valeurs
ma_serie.iloc[-2:]
```
### Méthodes des objets de classes `Series`
[Doc](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)

| méthodes pour les séries |                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `describe()`             | affiche un résumé statistique sur les valeurs de la série :<br>`count`  nombre sans compter les valeurs manquante<br>`mean`    moyenne <br>`std`      déviation standard écart type<br>`min`      valeur minimum<br>`25%`      quartiles ,divise le données en 4 parts égales<br>`50%`      des individus font moins que la valeur<br>`75%`      des individus font moins que la valeur<br>`max`      valeur maximum |
| `value_count()`          | visualise les valeurs uniques et leurs nombre                                                                                                                                                                                                                                                                                                                                                                        |
| `replace()`              | remplace une ou +ieurs valeurs par une autre                                                                                                                                                                                                                                                                                                                                                                         |
| `set_index()`            | redéfini les index                                                                                                                                                                                                                                                                                                                                                                                                   |





### Ajouter, supprimer modifier des valeurs d'une `Serie`

La méthode `append()`permet de concaténer des `Series`
On donne un objet de type `Serie`à la méthode `append()`
une liste de valeurs et une liste optionnelle d'index correspondant 

Par sécurité, `append()`retourne une copie (un nouvel objet) et n'applique pas le traitement sur l'objet original

On peut lui assigner le même nom pour forcer le changement de l'original

```python
ma_serie =
ma_serie.append(pd.Series([liste_valeurs], index=["liste de label"]))
```

### Supprimer une valeur d'une `Serie`

méthode `drop()`
supprime les valeurs aux étiquettes d'index spécifié en option.

```python
ma_serie.drop(labels=["index_1", "index_2"], inplace=False)
```

| option `inplace` | n'existe pas dans la méthode `append()`            |            |
| ---------------- | -------------------------------------------------- | ---------- |
| `inplace=False`  | la modification est effectuée sur une copie        | par défaut |
| `inplace=True`   | la modification est effectuée sur l'objet original |            |








### Modifier les valeurs d'une `Serie`
indexeurs `loc`et `iloc`
```python
ma_serie.loc["nom_index"] = nouvelle_valeur
# ou
ma_serie.loc["nom_index_1", "nom_index_2"] = [nouvelle_valeur_1, nouvelle_valeur_2]
# ou
ma_serie.iloc[position] = nouvelle_valeur
```

Avec `loc`, si un nom d'index a plusieurs occurences, elle seront toutes modifiées
Avec `iloc`une seule occurence serait modifiée ( les positions sont unique )




---
---
## `Dataframe`

objet, structure de donnée, tableau à 2 dimensions

- Les index des lignes : axe 0 ↓
et
- les noms de colonnes : axe 1 →

permettent d'accèder aux données
Reprend les mêmes paradigmes que les ndarray de [[Numpy]]

| `axis`   | Direction    | Cela veut dire                                                           |
| -------- | ------------ | ------------------------------------------------------------------------ |
| `axis=0` | vertical  ↓  | **On opère sur les lignes**, on applique l'opération colonne par colonne |
| `axis=1` | horizontal → | **On opère sur les colonnes**, on applique l'opération ligne par ligne   |


| Pandas    | Slice python | veut dire                              |
| --------- | ------------ | -------------------------------------- |
| `df.iloc` | `[:,-1]`     | toutes les lignes, la dernière colonne |
| `df.iloc` | `[:-1]`      | toutes les lignes sauf la dernière     |
| `df.iloc` | `[:, :-1]`   | toutes les colonnes sauf la dernière   |



| index | A   | B   | C   |
| ----- | --- | --- | --- |
| 0     | 5   | 5   | 5   |
| 1     | 5   | 5   | 5   |
| 2     | 2   | 5   | 8   |
```python
# somme des colonnes (ligne par ligne pour chaque colonne)
df.sum(axis=0)
```
A = 12
B = 15
C= 18
```python
df.sum(axis=1)
```
0 = 15
1 = 15
2 = 15







```python
# Lire un fichier .txt
pd.read_table('chemin_du_fichier.txt')
# Lire un fichier csv
pd.read_csv('chemin_du_fichier.csv')

'''La seule différence entre ces 2 fonctions est la valeur de l'option séparateur :
sep = "/t"      (tabulation en python)
sep = ","
sep = ";"
sep = " "
'''

# enregistrer le dataframe dans une variable
nom_dataframe = pd.read_csv('nom_du_fichier.csv')
# affiche les 5 première lignes pour vérifier l'import
nom_dataframe.head()

# Lire un fichier json
pd.read_json('nom_du_fichier.json')

# Lire un fichier excel
pd.read_excel('nom_du_fichier.xlsx')
```

Par défaut, les fonctions de lecture de fichier de Pandas créent un `DataFrame`, même à partir d'un fichier avec une seule colonne.

Les données sont représentées et manipulées sous un format de tableau en python:
- chaque <font color="orange">ligne</font> représente un <font color="orange">individu</font> ou <font color="orange">observation</font>
- chaque <font color="orange">colonne</font> une <font color="orange">variable</font>.
- <font color="orange">chaque colonne peut être d’un type différent, mais une colonne ne peut contenir qu’un seul type !</font>

L’objet `DataFrame` de Pandas permet de manipuler simplement et efficacement les données et accéde facilement aux caractéristiques générales des jeux de données :

- comme les types de variables
- le nombre de lignes
- le nombre de colonnes
- etc ...

### caractéristique globale du data frame

```python
nom_dataframe.shape
```

retourne un tuple :  ( nombre de lignes,  nombre de colonnes)

```python
dim = nom_dataframe.shape
print(dim[0]) # 228 lignes
print(dim[1]) #   4 colonnes
```

- la méthode  `.head()`  sélectionne par défaut les 5 premières lignes du data frame.     
- la méthode  `.tail()`  sélectionne par défaut les 5 dernières lignes du data frame. 
- Il est possible de préciser entre parenthèses le nombre de lignes à afficher

Types de chacune de nos variables. On peut accéder à cela très simplement à partir de l’attribut  `.dtypes`  :

```python
nom_dataframe.dtypes
```

Transformer un data frame en array :

```python
clients_array = nom_dataframe.values
display(clients_array)
```

### Naviguer dans un data frame

Accéder à une colonne (variable) d’un data frame, il suffit d’utiliser la syntaxe
```python
nom_dataframe[nom_variable]
```

Stocker dans une variable la variable 'email' du dataframe :
```python
email = nom_dataframe['email']
```

Accéder à plusieurs colonnes (variables)

- stocker les noms des colonnes dans une liste :
```python
variables = ['nom', 'email']
nom_dataframe[variables]

# version courte :
nom_dataframe[['nom', 'email']]
```
Les variables s’affichent dans l’ordre spécifié, sans modifier le data frame initial.


### indexing d'un `DataFrame`

Comme avec les `Serie`mais il faut donner 2 ensembles de valeurs, 1 pour les lignes, 1 pour les colonnes.

#### indexing et slicing avec l'attribut `loc`
sélectionne les données selon les étiquettes des lignes et le noms de colonnes
```python
# sélectionne une valeur unique
dataframe.loc["nom_ligne", "nom de colonne"]
# sélectionne 2 valeurs sur 2 lignes et une seule colonne
dataframe.loc[["nom_ligne", "nom_ligne_2"], ["nom_de_colonne", "nom_de_colonne"]]
# sélectionne une ligne et toutes les colonnes
dataframe.loc["nom_ligne", :]
# sélectionne toutes les lignes et une colonne
dataframe.loc[:, ["nom_de_colonne"]]

```




 ### Modifier une colonne (variable)

Pour modifier ou créer une colonne`col` , la syntaxe sera : 
```python
mon_dataframe['col'] = x
```
où `x` représente soit une valeur fixe, soit un objet de même dimension que la colonne qu’on souhaite modifier/créer.

### Supprimer une colonne (variable)

Il existe officiellement 3 façons :

1. La méthode`.drop`
```python
nom_dataframe.drop(columns='id')
```
<font color='orange'>La méthode `.drop` ne modifie pas le data frame existant.</font>
Elle renvoie une de copie du data frame en y ayant appliqué les modifications – ici supprimer la colonne id.

Vous aurez besoin de remplacer votre data frame pour pallier cela :
```python
nom_dataframe = nom_dataframe.drop(columns='id')
```

2. Le mot clé `del` 
```python
del nom_dataframe['id']
```

3. la méthode`.pop` 
```python
nom_dataframe.pop('id')
```

### Renommer une ou plusieurs colonnes
```python
mon_dataframe.rename(columns={'ancien nom': 'nouveau nom'})
data.rename(columns={'identifiant': 'ide','email': 'mail'})
```

<font color='orange'>La méthode `rename` ne modifie pas le data frame existant</font>.
Il existe un argument pour cette méthode (et pour toutes les méthodes similaires) nommé  `inplace` , qu’il suffit de fixer à `True` :

```python
data.rename(columns={'identifiant': 'ide'}, inplace=True)  

# est strictement équivalent à  

data = data.rename(columns={'identifiant': 'ide'})
```

### Changez le type d’une colonne

#### La méthode`.astype` permet de changer le type d’une colonne :
Il faut préciser le type entre parenthèses
```python
data['identifiant'].astype(float)
```


#### La méthode`.to_numeric`
```python
pd.to_numeric(arg, errors='raise', downcast=None)
```
Paramètres :
1. **`arg`** :
    - Les données à convertir (peut être une liste, une série, ou un DataFrame).
    - Exemple : Une colonne contenant des chaînes comme `'123'`, `'45.67'`.
2. **`errors`** :
    - Contrôle comment les erreurs sont gérées lors de la conversion.
    - Options :
        - **`'raise'`** (par défaut) : Lève une erreur si une valeur ne peut pas être convertie.
        - **`'coerce'`** : Remplace les valeurs non convertibles par `NaN`.
        - **`'ignore'`** : Laisse les données inchangées si elles ne peuvent pas être converties.
3. **`downcast`** :
    - Essaie de réduire la précision des données pour économiser de la mémoire.
    - Options : `'integer'`, `'float'`, ou `'unsigned'`.

Retourne :

- Une **`Series`** ou un **`DataFrame`** (selon l'entrée), où les valeurs sont converties en types numériques (`int64`, `float64`, etc.).

### Valeurs unique ?

méthode `nunique()` pour compter le nombre de valeurs uniques dans la colonne. Si le résultat est 1, toutes les valeurs sont identiques :

```python
# Vérifier si toutes les valeurs sont identiques
if mon_dataframe['ma_colonne'].nunique() == 1:
	print("Toutes les valeurs de ma_colonne sont identiques.")
else:
	print("Toutes les valeurs de ma_colonne ne sont pas identiques.")
```

### Triez un data frame `.sortvalues`

La méthode`.sort_values` 
Préciser entre parenthèses la ou les colonnes selon lesquelles il faut trier :

```python
# trier selon l’identifiant, par ordre croissant :
data.sort_values('identifiant')

#trier selon l’identifiant par ordre décroissant :
data.sort_values('identifiant', ascending = False)

# trier selon le genre puis le nom, par ordre croissant :
data.sort_values(['genre', 'nom'])

# par genre en ordre croissant et par nom en ordre décroissant
clients.sort_values(['genre', 'nom'], ascending=[True, False])
```

- On peut sélectionner une ou plusieurs colonnes d’un data frame via la syntaxe  `mon_dataframe[col]`, où `col` est soit le nom de la colonne à sélectionner (lorsqu’il n'y en a qu’une), soit une liste de noms de colonnes (lorsqu’il y en a plusieurs).

- Pandas trie par colonne par défaut

- Une colonne d’un data frame est une série Pandas.

- De nombreuses manipulations sont possibles avec/via des séries ; on peut notamment :

    - modifier, ajouter ou supprimer une colonne
    - modifier le nom d’une colonne via la méthode`.rename()`
    - changer le type d’une colonne via la méthode`.astype()` 
    - trier un data frame via la méthode`.sort_values()`


###  Filtrer des données `.loc .i`loc`

### méthode`.iloc`
permet de sélectionner à partir des indices
```python
mon_dataframe.iloc[indice_ligne, indice_colonne]
```

   sélectionner toutes les colonnes des 10 premières ligne de l'array 'clients' :
```python
clients.iloc[:10, :]
```

   sélectionner les colonnes 2 et 4 des 10 dernières lignes :
```python
clients.iloc[-10:, [1, 3]]
```

### méthode `.loc`
permet de sélectionner.

```python
mon_dataframe.loc[ index _lignes, index_colonne ]

mon_dataframe.loc[ condition sur les lignes, colonne(s) ]
```

### <font color='red'>indices</font>
position intrinsèque d’un élément au sein d’un tableau.
est <font color='red'>relatif aux opérations réalisées</font>.

### <font color='red'>index</font>
<font color='red'>une ligne</font> - quelle que soit sa position dans le data frame - <font color='red'>aura toujours le même index</font>
peu importe les opérations effectuées.
C'est une valeur unique qui est associée intrinsèquement à chaque ligne, sur la gauche du data frame.
Par défaut, ils correspondent aux indices.
Peuvent ne pas être numériques


Il est possible de réinitialiser ce dernier via la méthode  `.reset_index` .
### méthode `.reset_index()`

- La condition sur les lignes est une condition qui va être testée sur chaque ligne.
  Une ligne est conservée dans le processus de sélection si elle satisfait à cette condition.
  Cette condition peut être une conjonction de plusieurs conditions séparées par des "et" logiques (`&` ) ou des "ou" logiques (`|` )

- Les index sont des valeurs qui sont associées intrinsèquement à chaque ligne. Si on effectue un tri ou toute autre opération, une ligne, quelle que soit sa position dans le data frame, aura toujours le même index. Il est possible de réinitialiser ce dernier via la méthode  `.reset_index` 

- La méthode`.loc` peut être également utilisée pour modifier la partie du data frame sélectionnée.
### Résumé
- Il existe deux méthodes pour sélectionner précisément des éléments au sein d’un data frame : 

    - La méthode`.iloc` permet de sélectionner à partir des indices. La syntaxe est :  `mon_dataframe.iloc[ indice(s) ligne ,  indice(s) colonne ]`  .

    - La méthode`.loc` permet de sélectionner à partir de conditions et des noms de colonnes. La syntaxe est :  `mon_dataframe.loc[ condition sur les lignes ,  colonne(s) ]`  .

- La condition sur les lignes est une condition qui va être testée sur chaque ligne. Une ligne est conservée dans le processus de sélection si elle satisfait à cette condition. Cette condition peut être une conjonction de plusieurs conditions séparées par des :
	- `&`    "et" logiques
	- `|`    "ou" logiques 


- Les index sont des valeurs qui sont associées intrinsèquement à chaque ligne. Si on effectue un tri ou toute autre opération, une ligne, quelle que soit sa position dans le data frame, aura toujours le même index. Il est possible de réinitialiser ce dernier via la méthode  `.reset_index` .

- La méthode`.loc` peut être également utilisée pour modifier la partie du data frame sélectionnée.





---
## Agréger des données`.group_by` et `.pivot_table

 Une **agrégation** est une opération très courante sur des data frames, soit pour analyser les données sous un certain angle, soit pour recalculer certaines variables
### Agrégez des lignes

La première méthode pour faire une agrégation avec Pandas est **`.group_by`** . 

1. Se **fixer** sur une ou plusieurs colonnes, qui seront ce qu’on appelle les **index** du résultat agrégé. L’index permet de créer plusieurs groupes : un pour chaque valeur unique de l’index.
2. Choisir une **fonction d’agrégation**. La fonction d’agrégation va prendre en entrée un groupe de plusieurs lignes, pour effectuer un calcul sur celles-ci dans l’optique de retourner _une unique valeur pour chacun des groupes_

C'est similaire à l’opération de GROUP BY réalisable en [[SQL]]

##### **Exemple  1 :**
On souhaite calculer la moyenne de la variable`col` pour chaque valeur de la variable`fix` . 
![.group_by](img/pandas/group_by_1.bmp)

```python
dataframe.groupby('fix').mean()
```

Dans un premier temps, notre index sera la variable`fix` 
2 groupes sont créés, un pour chaque valeur dans la variable`fix` .
![.group_by](img/pandas/group_by_2.bmp)

Sur chacun de ces groupes, on applique la fonction d’agrégation choisie (moyenne).
#### **Exemple 2 : Agences bancaires qui font des prêts dans plusieurs villes**

Le chiffre d'affaires total de chacune des agences

```python
prets.groupby('agences').sum()
```

Le chiffre d'affaires total par agence ET par type de prêt 
transmettre la liste des variables à placer en index

```python
prets.groupby(['ville', 'type']).sum()
```

Avoir le résultat seulement sur la variable _remboursement_ :

```python
prets.groupby(['ville', 'type'])['remboursement'].sum()
```

Appliquer plusieurs fonctions d’agrégation sur une même colonne.
Appliquer des fonctions d’agrégation différentes en fonction de la colonne.

Calcul la moyenne et la somme de`remboursement` par agence, ainsi que le maximum de`revenu`  :

```python
prets.groupby('ville').agg({'remboursement': ['sum', 'mean'],
    'revenu': 'max'})
```

<font color='orange'>Avec `group_by` , les variables fixées en index se retrouvent… en index.</font> C’est-à-dire que si vous essayez d’accéder à la variable`ville` du résultat du _group by_, vous aurez simplement une erreur !
Il faut effectuer un`reset_index` pour la replacer en “colonne”.

### Agrégez des lignes et des colonnes

méthode **`.pivot_table`** prend 4 arguments en paramètres :

- **index** : variable(s) placée(s) en ligne ;
- **columns** : variable(s) placée en colonne(s) ;
- **values** : variable sur laquelle on va appliquer la fonction d’agrégation ;
- **aggfunc** : fonction d’agrégation.

La méthode permettant la transformation inverse s’appelle **`melt`** .





## Fusionner des données `.concat` et `.merge`

Il existe deux façons de _fusionner_ deux data frames : 

- si les data frames ont la même structure, on peut faire une concaténation via la fonction `concat` : mettre les 2 data frames bout à bout 

- sinon, on peut faire une jointure via les fonction/méthode`merge` .
### Concaténer des données
Syntaxe :
Placer l’ensemble des dataframes dans une liste, et utiliser la fonction `concat` sur cette liste.
```python
liste_concat = [dataframe_1, dataframe_2]
pd.concat(liste_concat)
```
La **concaténation** assemble plusieurs data frames qui ont la même structure
mêmes colonnes,  mêmes types.

 Ce n'est pas une [jointure](Pandas.md#jointure) (dimension horizontale)
 La concatenation mets l’un à la suite de l'autre (dimension verticale)
 Comme lors d’un ajout d'élément à une liste, via la méthode  `append`

<font color='orange'>La concaténation ne gère pas du tout les index par défaut.</font>
elle met juste le second data frame à la suite du premier, ainsi il y a des index en doublon.

Pour éviter cela, on peut utiliser l’argument`ignore_index` , qui équivaut à appliquer une méthode`reset_index`  :  
```python
pd.concat([df1, df2], ignore_index=True)
```
### jointure

Permet de joindre les informations de 2 data frames à partir d’une clé, une variable commune aux 2 data frames. La **clé** peut être formée d’une ou plusieurs colonnes

Le fait de rassembler plusieurs jeux de données différents est appelé une **jointure**, en algèbre relationnelle.

l’opération est quasi équivalente à une jointure qu’on pourrait réaliser en SQL
mais les **clés primaires** et **étrangères** ne sont pas explicitement identifiées dans un data frame Python.

Il existe deux façons de faire une jointure entre 2 data frames  `A` et`B`  avec Pandas :
- la fonction `merge`
- la méthode `merge`
```python
# fonction Pandas :
pd.merge(A, B)
# méthode de data frame :
A.merge(B)
```
 mêmes arguments, mêmes résultats
 
**jointure naturelle** :
Par défaut, Pandas va chercher les colonnes en commun dans les différents data frames (celles qui portent le même nom) et va les sélectionner comme clés

**Si on spécifie la clé**  :

- argument`on`
  La clé porte le même nom dans chaque data frame

- arguments`right_on`  et  `left_on`
  précise quelle clé on va utiliser dans chaque data frame, droite et  gauche

#### Exemples :

Jointure jointure simple sur une clé `id` entre 2 data frames A et B

```python
pd.merge(A, B, on='id')
```

Jointure entre 2 dataframes C (`left`) et A (`right`)
Effectue la jointure sur a clé`identifiant` du data frame C
avec la clé `id` du data frame A
```python
C.merge(A, left_on='identifiant', right_on='id')
```

Le data frame `left` est le premier renseigné, donc A, avec la clé `id`
Le data frame `right` est B, avec la clé `identifiant`

```python
pd.merge(A, B, left_on='id', right_on='identifiant')
```

### Explorez les différents types de jointure

Avec Pandas, il est indispensable de fixer le type de jointure pour déterminer comment traiter les différentes clés des data frames

Notamment lorsqu’il y a des soucis de correspondance – une clé présente dans un data frame mais pas dans l’autre.

Il existe 4 types de jointures, qui sont toutes focalisées sur les différentes clés :

| interne  | `inner join` |
| -------- | ------------ |
| à gauche | `left join`  |
| à droite | `right join` |
| externe  | `outer join` |
- la jointure interne conserve les clés se trouvant dans le premier ET le second data frame 

- la jointure à droite (ou à gauche) qui conserve uniquement les clés se trouvant dans le data frame à droite (ou à gauche), et complète les informations manquantes par des valeurs manquantes, ou`NaN` ;

- la jointure externe qui conserve toutes les clés se trouvant dans le premier OU le second data frame.
 
