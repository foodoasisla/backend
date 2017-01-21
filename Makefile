test:
	REUSE_DB=1 ./manage.py test

setup:
	pip install -r requirements.txt
	psql -c 'DROP database IF EXISTS la_food_oasis;'
	psql -c 'DROP database IF EXISTS la_food_oasis_test;'
	psql -c 'DROP ROLE IF EXISTS la_food_oasis_user;'
	psql -c 'create user la_food_oasis_user;'
# don't love this but superuser is needed in order to add postgres extensions...
	psql -c 'ALTER USER la_food_oasis_user SUPERUSER;'
	psql -c 'create database la_food_oasis owner la_food_oasis_user;'
	python manage.py migrate
	mkdir -p csv_files
	python manage.py csv_ingest
