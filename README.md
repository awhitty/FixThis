# FixThis
*We're making the world a better place here.*

## Requirements
* [Virtualenv.py](https://raw.github.com/pypa/virtualenv/master/virtualenv.py)
* Python 2.7 (ish)

### Set up/Installation
1. Clone the repository
2. Run something like `virtualenv.py env` to create a new virtual environment in the repo
	* I'd recommend naming it `env` since this is in the `.gitignore` file
	* This will also install pip in the environment, which is nice
3. Now activate the virtual environment using `source env/bin/activate`
4. Install all of the dependencies for the app using `pip install -r requirements.txt`
5. You can now (hopefully) run `python manage.py runserver` to test the app
6. If you have [foreman](http://theforeman.org) installed, you can run `foreman start` to test the production server ([gunicorn](http://gunicorn.org))