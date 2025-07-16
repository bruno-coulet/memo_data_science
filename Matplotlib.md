[Documentation](https://matplotlib.org/3.5.0/index.html)
[Cheat sheet](matplotlib_cheatsheets.pdf)

le module **`pyplot`** de la bibliothèque **`matplotlib`** permet de faire des graphes.
```python
import matplotlib.pyplot as plt
```


Librairie de [[Python]] utilisée pour la data visualisation
calquée sur **MATLAB**, un langage utilisé en calcul scientifique 

Sert de base à [[Seaborn]]

Chaque représentation graphique a une fonction correspondante avec Matplotlib :

| Représentation graphique          | Fonctions Matplotlib |
| --------------------------------- | -------------------- |
| nuage de points (scatter plot )   | `scatter()`          |
| diagrammes en ligne ou en courbes | `plot()`             |
| diagrammes en barres              | `bar()`              |
| histogrammes                      | `hist()`             |
| diagrammes circulaires            | `pie()`              |

## Nuage de points
[Documentation de la fonction`scatter`](https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.scatter.html)
2 variables numériques, sans évolution dans le temps
nécessite de définir les valeurs à placer en abscisse et en ordonnée :
```python
plt.scatter(dataframe['valeurs_x'], dataframe['valeurs_y'])
```
#### options du nuage de points
```python
plt.scatter(dataframe['valeurs_x'], dataframe['valeurs_y'],
    s=60, alpha=0.5, c='red', marker='P')
```

| argument      | personnalisation        |
| ------------- | ----------------------- |
| `color` ou`c` | couleur des points      |
| `size` ou`s`  | taille des points       |
| `marker`      | type de marqueur        |
| `alpha`       | transparence des points |
## Diagramme circulaire
[Documentation de la fonction`pie`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html)

fonction`pie` prend 2 arguments :
1. labels , correspondant à la variable non numérique, celle sur laquelle ont été agrégées les données
2. x, les valeurs agrégées correspondantes.
```python
plt.pie(x=data['valeurs_agreges'], labels=data['etiquettes'])
```

 La première étape va donc être d’agréger les données :
 Le`reset_index` est nécessaire si on a besoin de la variable  `ville` dans la création des prochains graphiques.
```python
data = prets.groupby('ville')['remboursement'].sum()
data = data.reset_index

plt.pie(x=data['remboursement'], labels=data['ville'])
```

#### options du diagramme circulaire
Afficher les pourcentage des parts avec 2 chiffres après la virgule suivie du caractère`%`
```python
plt.pie(x=data['remboursement'], labels=data['ville'], autopct='%.2f%%')
```


## Diagramme à barres
[Documentation de la fonction`bar`](https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.bar.html)
fonction`bar` prend deux arguments :

1. x : les différentes valeurs de la variable non numérique, l’équivalent du`labels` de`pie`
2. `height` : les valeurs agrégées, équivalent du `x`  de `pie` .

```python
# par défaut : d'abord x, puis y
plt.bar(data['ville'], data['remboursement'])

# Equivalent à :
plt.bar(height = data['remboursement'], x = data['ville'])
```

Pour ordonner du plus grand au plus petit, il faut trier le data frame en amont.
```python
data_sorted = data.sort_values('remboursement', ascending=False)
plt.bar(height=data_sorted['remboursement'], x=data_sorted['ville'])
```

## Histogramme
[Documentation de la fonction `hist`](https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.hist.html)
La fonction `hist` prends en paramètre la variable numérique dont on souhaite connaître la distribution
```python
plt.hist(prets['revenu'])
```

## Courbes
[Documentation de la fonction `plot`](https://nbviewer.org/urls/gist.githubusercontent.com/Jwink3101/e6b57eba3beca4b05ec146d9e38fc839/raw/f486ca3dcad44c33fc4e7ddedc1f83b82c02b492/Matplotlib_Cheatsheet)
La fonction `plot`prend 2 arguments : les informations en abscisse, et celles en ordonnée.
```python
plt.plot(evolution_ca['date'], evolution_ca["chiffre d'affaire"])
# Avec options
plt.plot(evolution_ca['date'], evolution_ca["chiffre d'affaire"],
marker='o', linestyle='--', color='red')
```

| argument      | personnalisation        |
| ------------- | ----------------------- |
| `color` ou`c` | couleur des lignes      |
| `linestyle` ou `ls`  | style des lignes       |
| `linewidth` ou `lw`     | épaisseur        |
| `marker`       |  marqueur suplémentaire  |

## Personnalisation
[notebook d'exemple de personnalisation](https://nbviewer.org/urls/gist.githubusercontent.com/Jwink3101/e6b57eba3beca4b05ec146d9e38fc839/raw/f486ca3dcad44c33fc4e7ddedc1f83b82c02b492/Matplotlib_Cheatsheet)

- Eléments externes avec les fonctions  :
    - un titre,  fonction`title`
    - une légende, fonction`legend`
    - les titres des axes, `xlabel` et `ylabel`

- Modifiez de nombreux éléments internes à notre visualisation :
    - graduations, fonction`xticks` ou`yticks` 
    - du texte à un emplacement précis, fonction `text` 
    - quadrillage, `grid` 
    - éléments graphiques spécifiques, fonction`rc` .

## Exemple
```python
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.patches import Rectangle

def plot_unordered_list(unordered_list):
    plt.figure(figsize=(10, 5))
    plt.plot(unordered_list, color='gray', label='Non triée')
    plt.xlabel('Indice des éléments')
    plt.ylabel('Valeurs aléatoires')
    plt.title('Liste non triée')
    plt.legend()
    plt.tight_layout()
    plt.show()

        plt.figure(figsize=(10, 10), facecolor='black')

        # Normalize the sorted list to map it to colors
        norm = Normalize(vmin=min(sorted_list), vmax=max(sorted_list))
        # Create a colormap
        cmap = plt.get_cmap('viridis')
                # Normalize the sorted list to map it to colors

        norm = Normalize(vmin=min(sorted_list), vmax=max(sorted_list))

        # Create a colormap

        cmap = plt.get_cmap('viridis')

colors = [cmap(norm(value)) for value in sorted_list]
```



### Plusieurs graphiques

```python
# Créer la figure et les axes (les différents graphiques)
fig, axs = plt.subplots(2, 1, figsize=(8, 6))
# Premier graphique : sinus
axs[0].plot(x, y1, label='sin(x)', color='blue') axs[0].set_title("Graphique de sin(x)", color='white') axs[0].legend() axs[0].set_facecolor('#111111')

# Deuxième graphique : cosinus
axs[1].plot(x, y2, label='cos(x)', color='red') axs[1].set_title("Graphique de cos(x)", color='white') axs[1].legend() axs[1].set_facecolor('#111111')
 
# Ajuster l'espacement entre les graphiques
plt.subplots_adjust(hspace=0.4)
```

- **`plt.subplots(nb_de_lignes, nb_de_colonnes)`** : Crée une grille d'axes avec `nrows` lignes et `ncols` colonnes.
    
    - `axs` est un tableau ou une liste contenant les axes.
- **Manipuler chaque graphique individuellement :**
    - `axs[0]` fait référence au premier graphique.
    - `axs[1]` fait référence au deuxième graphique.