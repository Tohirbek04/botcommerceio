mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

cat_fixture:
	python3 manage.py loaddata shop_category.json
