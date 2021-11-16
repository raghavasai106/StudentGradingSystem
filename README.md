# StudentGradingSystem 
install python 3 and open in an IDE, I have used PyCharm Pro.
# Create virtual enivornment 
Source venv/bin/activate
(In Pycharm, it automatically launches the virtual environment when cloned).
# Install requirements file containing Django and forms 
pip install -r requirements.txt
# To create DB
python manage.py makemigrations
python manage.py migrate
# Run the application 
python manage.py runserver 

