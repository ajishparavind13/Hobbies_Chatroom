<div align="center">


# Hobbies-Chatroom
</div>

### Cloning the repository

--> Clone the repository using the command below :
```bash
https://github.com/ajishparavind13/Hobbies_Chatroom.git

```

--> Move into the directory where we have the project files : 
```bash
cd Hobbies-Chatroom

```

--> Create a virtual environment :
```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv env

```

--> Activate the virtual environment :
```bash
env\scripts\activate

```

--> Install the requirements :
```bash
pip install -r requirements.txt

```
--> Create a super user in admin page :

``` bash
python manage.py migrate --run-syncdb
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
#

### Running the App

--> To run the App, we use :
```bash
python manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

#

### App Preview :

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
  Feed Home
</p>
<img src="https://user-images.githubusercontent.com/72341453/134747262-0a92233d-8010-40f8-84c5-8d94895aac44.PNG">
</td> 
<td width="50%">
<br>
<p align="center">
  Room Conversation Preview
</p>
<img src="https://user-images.githubusercontent.com/72341453/134747155-3ca5b55f-b064-4741-aeae-abe90bddf41e.PNG">  
</td>
</table>


#For detailed - information do visit our blogpost https://medium.com/@ajishparavind13/deploying-a-django-chatroom-app-on-aws-step-by-step-guide-843951ee90ab
