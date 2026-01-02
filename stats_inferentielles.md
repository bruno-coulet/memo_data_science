# Statistique inferentielles

Permettent de généraliser des propriété à une population, à partir d'un échantillon de données

Les phénomènes observés dans l'échantillon de données peuvent-ils se généraliser à l'ensemble dune population ?

## Tests d'hypothèses

Tous les tests reposent sur la formulation de **2 hypothèses** :
- hypothèse nulle `H0` : situation de base
- hypothèse alternative `H1` : changement

Evalue la probabilité que l'hypothèse nulle (pas de changement) soit vrai<br>
Si cette probabilité est trop faible, inférieure à un seuil, alors `H0` est rejettée en faveur de `H1`<br>
suggère la présence d'un effet ou d'un changement

### p-value
probabilité utilisée pour invalider ou non H0

Si `p-value` < seuil (5% en général)<br>
on rejette H0 et adopte H1

### Significativité

Le résultat du test est significatif au seuil des 5% (en général)

Si la `p-value` est extremement faible :
- le résultat est très **significatif**
- `H0` étant très en dessous du seuil, à une très faible probabilité de se produire


### Marge d'erreur
mesure statistique qui quantifie l'incertitude liée à la taille de l'échantillon étudié<br>
Plus l'échantillon est important, plus la marge d'erreur diminue<br>
Par exemple :<br>
score annoncé de 54 % avec un intervalle de confiance à 95 % de [51,9;56,1]<br>
Signifie :
- 95 % de chance d'avoir un score entre 51,9% et 56,1%
- 5 % de chance d'avoir un score en dehors de cet intervalle de confiance
