# 1) python3 -m venv venv - создаём виртуальное окружение
# sourve venv/bin/activate
# pip freeze - показывает список уствновленных библиотек
# deactivate - выйти из виртуального окружения

############################################################

# 2) requirements.txt
    # django
    # djangoframework

# 3) pip install -r requirments.txt


# 4)django-admin starproject name_project . - создаём главное приложение нашего проекта

# 5) django-admin startapp new_name_app - создаём определённое приложение   
#  ./manage.py startapp new_name_app

# 6)
# ./manage.py makemigrations - создаёт миграцию
# ./manage.py migrate - применяет её

# ./manage.py createsuperuser - создаёт супер юзера

# ./manage.py runserver