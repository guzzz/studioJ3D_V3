**Project about a 3D images architecture company**

*Sample version just for portfolio avaliation of an existing system that runs in [STUDIO J3D Website](https://www.studioj3d.com.br).*

- The differences between this version (V3) and the previous ones are listed in the bottom of this Readme.

---

# STUDIO J3D (V3)

The system is very simple, and consists in five main areas.

1. **Home**: Shows one of the best 3D images produced by the company.
2. **Portfólio**: Shows all the 3D images produced by the company.
3. **Orçamento**: Explains how the company charges for their work.
4. **Sobre**: An 'about area', that explains what are the porposes of the company.
5. **Contato**: Contact area, where people can get the company's phone, their working hours and send an email to the company.

---

## Initial configuration

As this code is just for portfolio avaliation, you'll have to do some configurations before testing.

1. Our first step is into the **studioJ3D/studioJ3D/settings.py**. You have to generate one [python secret key](https://www.djecrety.ir/) and paste into the **SECRET_KEY** area (line 27).
2. Configure the sending email servidor. In this same archive, you'll have to set one new configuration between the lines 40 and 47. 
3. Configure the PostgreSQL database. You'll have to set one new configuration between the lines 103 and 112. 
4. Configure the AWS S3. You'll have to set one new configuration between the lines 167 and 174. 

---

## How to run the project

You have to do the following steps to create a virtual enviroment and then run the project.

1. First, you'll need Python 3.8.5 to run your project. So, let's create a virtualenv with this Python Version.
2. You'll need the command **python3 -m venv YOUR_VIRTUAL_ENV_NAME** to create the new env.
3. Then, you will have to activate your virtual env with the command: **source YOUR_VIRTUAL_ENV_NAME/bin/activate**.
4. After that, you will have to navegate to this projects folder, and do the following command: **pip install -r requirements.txt**. This command will install all project dependences.
5. To start the default database, you'll need to do the command: **python manage.py migrate** .
6. Now, let's create a superuser for Django Admin. You'll need to do the command: **python manage.py createsuperuser**.
7. Then, run this command: **python manage.py collectstatic**.
8. Finally, to run the project you will need to do the run command: **python manage.py runserver**.
If you have any questions about how to create a virtual env, please visit [the Django Girls Project Tutorial (in Portuguese)](https://tutorial.djangogirls.org/pt/django_installation/).

**Next time, you'll just have to activate the virtualenv and apply the "runserver" command.**

I've created a Makefile to run the project easily. However, you'll have to input some data in the archive before utilization. Once it's ready, run: **make start**.

---

## Features

This project contains an "Admin" area, where the user is able to fill the projects page and send emails to possible clients. Without an initial configuration on Django Admin, the projects page would shows yourself pretty empty. So, about the admin app:

1. To access the Admin area, you'll need to navegate to the url: "localhost:8000/admin" .
2. The projects page contains thumbnails inside DJANGO ADMIN to make listing more elegant. 
3. There is an area to send a default marketing mail to whoever you want.

**To use Django Admin, you'll have to have the superuser created on the previous section.**

---

## Major differences between the Studio J3D V3 and the previous ones. 

**V3 -> V2**
The Python and Django versions were updated. The database was changed to PostgreSQL. AWS S3 was implemented. The website now has support to 360º images. Filters from mobile version were remodeled. A Makefile was created. There was refactoring in some areas.


**V2 -> V1** 
The client realized that, unlike the "projects page", it was not necessary to update the "other pages" often in Django Admin. So, in this version we focused in creating a more elegant environment, pretty and simple.  All the pages were remodeled and the architeture was simplified. Filters were created on projects page, and we have more imagens and titles being shown in almost all pages. Google Analytics was implemented.

---

## Tools

* **Back-end**: Python 3.8.5 / Django 3.14 (Class-based views)
* **Front-end**: CSS/Bootstrap 4/Libraries to provide image visualization

---

## Purpose of this repository

* The owner has this sample version in a public repository just for show portfolio in their bitbucket. It's not for modifying, distribuition, or anything else that do not envolves portfolio avaliation. 