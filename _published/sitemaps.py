import os

from django.conf import settings


def items():
    items = [
        dict(
            location='/ipython-notebooks/aircraft-pitch-analysis-matlab-plotly',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'aircraft_pitch',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/ipython-notebooks/cufflinks',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'cufflinks',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/ipython-notebooks/survival-analysis-r-vs-python',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'survival_analysis',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/ipython-notebooks/amazon-redshift',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'redshift',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/ipython-notebooks/apache-spark',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'apachespark',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/ipython-notebooks/principal-component-analysis',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'principal_component_analysis',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/ipython-notebooks/big-data-analytics-with-pandas-and-sqlite',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'sqlite',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/ipython-notebooks/ukelectionbbg',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'ukelectionbbg',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/ipython-notebooks/salesforce',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'salesforce',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/ipython-notebooks/graph-gmail-inbox-data',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'gmail',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/ipython-notebooks/markowitz-portfolio-optimization',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'markowitz',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/ipython-notebooks/cartodb',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'cartodb',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/ipython-notebooks/network-graphs',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'networkx',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/ipython-notebooks/subplots',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'make_subplots',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/ipython-notebooks/basemap-maps',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'basemap',
                'body.html'),
            priority=0.5
        ),
        dict(
            location='/ipython-notebooks/collaboration',
            lmfile=os.path.join(
                settings.TOP_DIR,
                'shelly',
                'templates',
                'api_docs',
                'includes',
                'ipython_notebooks',
                'collaborate',
                'body.html'),
            priority=0.5
        )
    ]
    return items
