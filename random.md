
-  `random` (Module Standard Python)
pour des tâches simples, des projets de petite échelle ou si vous n’avez pas besoin de gérer de grandes quantités de données.


-  `numpy.random` (module de NumPy)
pour travailler avec des tableaux, des données volumineuses ou si besoin de distributions avancées ou de performances élevées.


### Random (Module Standard Python)

| **Fonction**                                    | **Description**                                                             | **Exemple**                                       |
| ----------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------- |
| `random.randint(a, b)`                          | Génère un entier aléatoire entre `a` et `b` inclus.                         | `random.randint(1, 10)`                           |
| `random.random()`                               | Génère un flottant aléatoire dans `[0.0, 1.0)`.                             | `random.random()`                                 |
| `random.uniform(a, b)`                          | Génère un flottant aléatoire dans `[a, b]`.                                 | `random.uniform(1.5, 6.5)`                        |
| `random.randrange(start, stop, step)`           | Génère un entier aléatoire dans la plage `[start, stop)` avec un pas donné. | `random.randrange(1, 10, 2)`                      |
| `random.choice(seq)`                            | Sélectionne un élément aléatoire d'une séquence (liste, tuple, chaîne).     | `random.choice(['a', 'b', 'c'])`                  |
| `random.choices(population, weights=None, k=1)` | Sélectionne `k` éléments avec ou sans pondération.                          | `random.choices(['a', 'b'], weights=[1, 2], k=3)` |
| `random.sample(population, k)`                  | Sélectionne `k` éléments uniques (sans répétition).                         | `random.sample(['a', 'b', 'c'], 2)`               |
| `random.shuffle(x)`                             | Mélange les éléments d'une liste en place.                                  | `random.shuffle([1, 2, 3])`                       |
| `random.seed(a)`                                | Fixe la graine pour rendre les résultats reproductibles.                    | `random.seed(42)`                                 |


### Random (module de Numpy)

| **Fonction**                            | **Description**                                                                               | **Exemple**                                              |
| --------------------------------------- | --------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| `np.random.randint(low, high, size)`    | Génère des entiers dans `[low, high)` (taille définie par `size`).                            | `np.random.randint(0, 10, size=(3, 3))`                  |
| `np.random.random(size)`                | Génère des flottants dans `[0.0, 1.0)` avec une taille spécifiée.                             | `np.random.random((2, 2))`                               |
| `np.random.uniform(low, high, size)`    | Génère des flottants dans `[low, high]` avec une taille spécifiée.                            | `np.random.uniform(1.5, 6.5, size=5)`                    |
| `np.random.normal(mean, std, size)`     | Génère des échantillons selon une distribution normale.                                       | `np.random.normal(0, 1, size=(3, 3))`                    |
| `np.random.binomial(n, p, size)`        | Génère des échantillons d'une distribution binomiale.                                         | `np.random.binomial(10, 0.5, size=10)`                   |
| `np.random.poisson(lam, size)`          | Génère des échantillons d'une distribution de Poisson.                                        | `np.random.poisson(3, size=10)`                          |
| `np.random.choice(a, size, replace, p)` | Sélectionne des éléments de `a` avec ou sans remplacement et des probabilités personnalisées. | `np.random.choice([1, 2, 3], size=5, p=[0.1, 0.2, 0.7])` |
| `np.random.seed(seed)`                  | Fixe la graine pour rendre les résultats reproductibles.                                      | `np.random.seed(42)`                                     |
|                                         |                                                                                               |                                                          |
 `randn`
génére des échantillons à partir d'une distribution normale standard
(distribution de Gauss) de moyenne 0 et d'écart type 1

### **Syntaxe :**

```python
numpy.random.randn(d0, d1, ..., dn)
```

### **Paramètres :**

- `d0, d1, ..., dn` : Dimensions de l'array de sortie. Ce sont des entiers qui spécifient la forme de l'array. Si aucun paramètre n'est fourni, un seul nombre aléatoire est retourné.

### **Retour :**

- Un array NumPy de la forme spécifiée, contenant des valeurs aléatoires tirées d'une distribution normale standard.

---

### **Exemples :**

#### 1. Générer un nombre aléatoire

python

Copier le code

`import numpy as np  valeur = np.random.randn() print(valeur)  # Exemple : -0.752759`

#### 2. Générer un tableau 1D

python

Copier le code

`array_1d = np.random.randn(5) print(array_1d)  # Exemple : [ 1.74481176 -0.7612069   0.3190391  -0.24937038  1.46210794]`

#### 3. Générer un tableau 2D

python

Copier le code

`array_2d = np.random.randn(3, 4) print(array_2d) # Exemple : # [[ 0.04153939 -1.11792545 -1.31590741 -1.39649634] #  [-0.69492057 -0.65092311 -0.09585941 -0.4216545 ] #  [-0.0577718  -0.60170661  1.85227818 -0.01349722]]`

#### 4. Générer un tableau 3D