master_doc = 'index'
project = "Endpoint: patrol"
copyright = '2020, Vanguard Security, Inc.'
author = 'Vanguard Security, Inc.'
version = release = ''

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
    'css/theme_overrides.css',  # override wide tables in RTD theme
]

def setup(app):
       app.add_stylesheet('custom.css')
