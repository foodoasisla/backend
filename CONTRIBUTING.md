# Getting Your Dev Environment Set Up - Mac & Windows

## Clone The Repo

Open a terminal and go to where you want to keep the project on your local machine.
Type `git clone https://github.com/foodoasisla/backend.git`

## Virtualenvwrapper - Mac

From a terminal window `pip install virtualenvwrapper`

Then add the following to your `.bashrc` file. Replace "Development_Directory" with the directory where your project lives.

    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/"Development_Directory"
    source /usr/local/bin/virtualenvwrapper.sh

After you save the file type `source ~/.bashrc`

run `mkvirtualenv temp` where "temp" is the name of the virtualenv you want to use.

A list of other virtualenvwrapper commands is located [here](http://virtualenvwrapper.readthedocs.io/en/latest/install.html).

##Postgres - Mac

Install Postgress from [here](http://postgresapp.com/)

Don't forget to set up your PATH. Instructions are [here](http://postgresapp.com/documentation/cli-tools.html)

Get into Postgres `psql`

If you get an error saying `psql: FATAL:  database "<user>" does not exist` do the following:

    createdb
    psql -h localhost

Create a user
    `CREATE USER la_food_oasis_user with password '[create password]';`

Create a database
    `CREATE DATABASE la_food_oasis OWNER la_food_oasis_user;`

Exit out of Postgres `\q`

##Postgres - Windows
Install Postgress from [here](http://www.enterprisedb.com/products-services-training/pgdownload#windows)

It may prompt you to create a password for superuser 'postgres'.

Set up your system PATH environment variables by adding file paths to bin and lib folders in the installed application folder, separated by semicolons. The paths may look like this: </br>
`C:\Program Files\PostgreSQL\9.6\bin;C:\Program Files\PostgreSQL\9.6\lib`

In the command line, test Postgres `psql --version`.

Get into postgres through the superuser account 'postgres' `psql -U postgres` and enter the password you set up on the install.

Create a user
    `CREATE USER la_food_oasis_user;`

Create a database
    `CREATE DATABASE la_food_oasis OWNER la_food_oasis_user;`

Exit out of Postgres `\q`

(To enter postgres as la_food_oasis_user you must enter the db name in addition to the username: </br>
`psql -U la_food_oasis_user la_food_oasis`)

##Install Dependencies

`(myvenv)~/backend pip install -r requirements`

##Migrate the Database

`(myvenv)~/backend/la_food_oasis python manage.py migrate`

##Populating data

drop into the django shell `python manage.py shell`
and run the following from within the shell `execfile('csv_ingest.py')
