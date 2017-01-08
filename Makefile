test:
	REUSE_DB=1 ./manage.py test

setup:
	# pip install -r requirements.txt
	# pip install django-nose
	psql -c 'DROP database IF EXISTS la_food_oasis;'
	psql -c 'DROP database IF EXISTS la_food_oasis_test;'
	psql -c 'DROP ROLE IF EXISTS la_food_oasis_user;'
	psql -c 'create user la_food_oasis_user;'
# don't love this but superuser is needed in order to add postgres extensions...
	psql -c 'ALTER USER la_food_oasis_user SUPERUSER;'
	psql -c 'create database la_food_oasis owner la_food_oasis_user;'
	python manage.py migrate
	mkdir -p csv_files
	curl https://gist.githubusercontent.com/worace/5b71323c36df2c77897f6deac7d337c6/raw/1b73beb412f2d869a913abe97495c5d10f9847c9/communitygardens.csv > ./csv_files/communitygardens.csv
	python manage.py csv_ingest
