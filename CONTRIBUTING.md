# Getting Your Dev Environment Set Up - Mac

## Clone The Repo

Open a terminal and go to where you want to keep the project on your local machine.
Type `git clone https://github.com/foodoasisla/backend.git`

## Virtualenvwrapper

From a terminal window `pip install virtualenvwrapper`

Then add the following to your `.bashrc` file. Replace "Development_Directory" with the directory where your project lives.

    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/"Development_Directory"
    source /usr/local/bin/virtualenvwrapper.sh

After you save the file type `source ~/.bashrc`

run `mkvirtualenv temp` where "temp" is the name of the virtualenv you want to use.

A list of other virtualenvwrapper commands is located [here](http://virtualenvwrapper.readthedocs.io/en/latest/install.html).

##Postgres

Install Postgress from [here](http://postgresapp.com/)

Don't forget to set up your PATH. Instructions are [here](http://postgresapp.com/documentation/cli-tools.html)

Get into Postgres `psql`

If you get an error saying `psql: FATAL:  database "<user>" does not exist` do the following:

    createdb
    psql -h localhost

Create a user
    CREATE USER la_food_oasis_user;

Create a database
    CREATE DATABASE la_food_oasis OWNER la_food_oasis_user;

Exit out of Postgres `\q`


##Install Dependencies

`(myvenv)~/backend pip install -r requirements`

##Migrate the Database

`(myvenv)~/backend/la_food_oasis python manage.py migrate