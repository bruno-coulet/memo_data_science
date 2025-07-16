[Documentation](https://docs.streamlit.io/)
[Crafting a dashboard](https://blog.streamlit.io/crafting-a-dashboard-app-in-python-using-streamlit/)

Framework python open source
Change des scripts de data (en python) en web app
Ne nécessite pas d'expertise front-end


```bash
pip install streamlit
# Pour voir la démo, vérifier si c'est installé :
streamlit hello

# Ou via conda :
conda install -c conda-forge streamlit
```


1. Utiliser des commandes Streamlit dans un script Python
2. Execute le script avec `streamlit run`:
```python
# Lancer
python -m streamlit run mon_script.py
# Equivalent de:
streamlit run mon_script.py
# ou encore un URL:
streamlit run https://raw.githubusercontent.com/streamlit/.../streamlit_app.py`
```
3. Un serveur local démarre l'app dans le navigateur
4. On met ce qu'on veux dedans :

 [`st.text`](https://docs.streamlit.io/develop/api-reference/text/st.text) écrit du text brut
 [`st.line_chart`](https://docs.streamlit.io/develop/api-reference/charts/st.line_chart) dessine un graphique en courbes
etc.. voir [la liste](https://docs.streamlit.io/develop/api-reference)

### Import libraries
- **Streamlit** - a low-code web framework
- [**Pandas**](https://pandas.pydata.org/?ref=blog.streamlit.io) - a data analysis and wrangling tool
- [**Altair**](https://pypi.org/project/altair/?ref=blog.streamlit.io) - a data visualization library
- [**Plotly Express**](https://plotly.com/python/plotly-express/?ref=blog.streamlit.io) - a terse and high-level API for creating figures  

Pour transmettre des arguments personnalisés dans le script, ils doivent être transmis après deux tirets. Sinon, les arguments sont interprétés comme des arguments de Streamlit.


```python
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
```

### Page configuration

Define settings for the app
giving it a page title and icon that are displayed on the browser. 
Defines the page content to be displayed in a wide layout that fits the page’s width
Show the sidebar in the expanded state.
Set the color theme for the Altair plot to be dark

```python
st.set_page_config(
    page_title="US Population Dashboard",
    page_icon="🏂",
    layout="wide",
    initial_sidebar_state="expanded")

alt.themes.enable("dark")
```
### Load data

Using Pandas’ `read_csv()` function :

```python
df_reshaped = pd.read_csv('data/us-population-2010-2019-reshaped.csv')
```
