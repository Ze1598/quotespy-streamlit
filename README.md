# quotespy_streamlit

A live demo of the quotespy Python library.

[quotespy](https://pypi.org/project/quotespy/) is a Python library developed by me to create quotes/lyrics and tweet graphics, based on the [Pillow](https://pypi.org/project/Pillow/) library.

This app was developed using [streamlit](https://docs.streamlit.io/en/stable/). As described in the documentation, "Streamlit is an open-source Python library that makes it easy to build beautiful custom web-apps for machine learning and data science".

The app is deployed on Heroku, available [here](https://quotespy-streamlit.herokuapp.com/). With it, you can create quotespy graphics on the web. In other words, you can create graphics similar to tweet screenshots and "free-form" graphics with centered text using the two modules available.

Lastly, a brief explanation of the files included in the repository:

* Procfile: ["Heroku apps include a Procfile that specifies the commands that are executed by the app on startup"](https://devcenter.heroku.com/articles/procfile)

* streamlit_app.py: Main script to manage the streamlit app

* requirements.txt: Text file with the application's dependencies (tip: it can be generated in your pipenv virtual environment using the command `pipenv lock -r > requirements.txt`)

* runtime.txt: Text file to specify the Python version to be used in Heroku

* setup.sh: Server setup on Heroku

* utils.py: Script with helper functions

* `static` directory: Static files (e.g. fonts in this case), must be located either in the root directory of the repository or inside this `static` directory