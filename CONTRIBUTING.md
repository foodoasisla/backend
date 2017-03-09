# Getting Your Dev Environment Set Up - Mac & Windows

## Clone The Repo

Open a terminal and go to where you want to keep the project on your local machine.
Type `git clone https://github.com/foodoasisla/backend.git`

## Python Version - Mac
Food Oasis LA runs on Python 3. Your Mac ships with Python 2.7. Some good instructions for installing Python 3 can be found [here](http://docs.python-guide.org/en/latest/starting/install3/osx/)

## Virtualenvwrapper - Mac

From a terminal window `pip install virtualenvwrapper`

Then add the following to your `.bashrc` file. Replace "Development_Directory" with the directory where your project lives.

    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/"Development_Directory"
    source /usr/local/bin/virtualenvwrapper.sh

After you save the file type `source ~/.bashrc`

You need to create a virtualenv with Python 3. 

Type `which python3` in your terminal. 
You will probably see something like this `/Library/Frameworks/Python.framework/Versions/3.5/bin/python3`. This is the location of your Python 3 interpreter.

run `mkvirtualenv --python=<location of your Python 3 interpreter> temp` where "temp" is the name of the virtualenv you want to use.

Your virtualenv will be activated after this step.

A list of other virtualenvwrapper commands is located [here](http://virtualenvwrapper.readthedocs.io/en/latest/install.html).

## Postgres - Mac

Install Postgress from [here](http://postgresapp.com/)

Don't forget to set up your PATH. Instructions are [here](http://postgresapp.com/documentation/cli-tools.html)

Get into Postgres `psql`

If you get an error saying `psql: FATAL:  database "<user>" does not exist` do the following:

    createdb
    psql -h localhost

Create a user
    `CREATE USER la_food_oasis_user;`

Create a database
    `CREATE DATABASE la_food_oasis OWNER la_food_oasis_user;`

Exit out of Postgres `\q`

## Postgres - Windows
Install Postgress from [here](http://www.enterprisedb.com/products-services-training/pgdownload#windows)

It may prompt you to create a password for superuser 'postgres'.

Set up your system PATH environment variables by adding file paths to bin and lib folders in the installed application folder, separated by semicolons. The paths may look like this: </br>
`;C:\Program Files\PostgreSQL\9.6\bin;C:\Program Files\PostgreSQL\9.6\lib`

In the command line, test Postgres `psql --version`.

Get into postgres through the superuser account 'postgres' `psql -U postgres` and enter the password you set up on the install.

Create a user
    `CREATE USER la_food_oasis_user with password '[create password]';`

Create a database
    `CREATE DATABASE la_food_oasis OWNER la_food_oasis_user;`

Exit out of Postgres `\q`

(To enter postgres as la_food_oasis_user you must enter the db name in addition to the username: </br>
`psql -U la_food_oasis_user la_food_oasis`)

## Install Dependencies - Mac

Make sure your virtualenv is activated. If it isn't type `workon <name of environment>`

Navigate in the terminal to the first backend folder, with the requirements.txt file. Install: </br>
`(myvenv)~/backend pip install -r requirements.txt`

## Install Dependencies - Windows

Navigate in the command line to the first backend folder, with the requirements.txt file. Install: </br>
`(myvenv)~/backend pip install -r requirements.txt`

## Configure Django Access to Database - Windows
Add a new system environment variable with name SECRET_KEY and with a secret key as the value.

Go to settings.py in the backend folder and go to line 95, where it says PASSWORD, uncommented. Add your database password between the quotes.

## Migrate the Database

`(myvenv)~/backend python manage.py migrate`

## Populating data

A sample dataset is located in backend/csv_files/

Run the Ingest Script by typing `python manage.py csv_ingest`

## Start the Server

```
(myvenv) ~/backend python manage.py runserver
```

Try out an endpoint:

```
curl -v localhost:8000/locations/
```
