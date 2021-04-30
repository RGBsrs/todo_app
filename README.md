# todo_app
ToDo app based on Vue.js and Flask framework


If you want test this project on your local machine run the following commands:

> git init
> git clone https://github.com/RGBsrs/flask_api_course.git
> 
Then create virtual enviroment:

> virtualenv env

Activate this enviroment:

>On Linux/Mac
>> env/bin/activate
>>
>On Windows
>> env/Scripts/activate

Install all dependencies:
> pip install -r requirements.txt

Init db:

>flask db init
>flask db migrate

Than run migrations:

> flask db upgrade

And now you can start this app:

> flask run
