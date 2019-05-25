import docs_italia_theme

discourse_url = 'https://forum.italia.it/'

extensions = [
    'docs_italia_theme',
    'sphinxcontrib.discourse'

]

master_doc = 'index'
html_theme = 'docs_italia_theme'
html_theme_path = [docs_italia_theme.get_html_theme_path()]
numfig = True
