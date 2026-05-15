Как запустить проект:

Клонировать репозиторий и перейти в него:

git clone https://github.com/roman23323/api-final-yatube-ad.git

cd api-final-yatube-ad

Создать и активировать виртуальное окружение:

python3 -m venv venv

source venv/bin/activate

Установить записимости из файла requirements.txt:

pip install -r requirements.txt

Выполнить миграции:

python3 manage.py migrate

Запустить проект:

python3 manage.py runserver