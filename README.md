# autohomeworks (Dissertation Project)


A web application which allows teachers to create courses, to invite students to those classes, 
create homeworks and automatically test the solutions proposed by the students.


This application is developed with [Django](https://www.djangoproject.com/) and supported by [Docker](https://www.docker.com/).

----------------------------

## Installation

1. Clone this repo:
      
        git clone https://github.com/dianaboiangiu/autohomeworks/
  
2. Install [Python 3.5](https://www.python.org/downloads/)

3. Install virtualenv

4. Create a virtual environment:
   
        virtualenv -p python3 venv

5. Activate the environment:
   
        venv/bin/activate .
   
6. Install the requirements:
   
        pip install -r requirements.txt
   
7. Apply migrations:
   
        python manage.py migrate
   
8. Start the server:
  
        python manage.py runserver
   
