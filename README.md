# CRL Assignment

The goal of this project is to implement a user listing solution in Django. 

Assingment statement is included on homepage.


<img width="1227" alt="Screenshot 2022-08-31 at 1 42 44 PM" src="https://user-images.githubusercontent.com/112490857/187628761-1a88146f-b156-4a2b-83a9-7ff2b1647c85.png">


### Main features

* Pre-defined number of users can be fetched from randomuser.me site.

* User list with pagination. Large data pagination handled in the code. 

* Realtime searching/filtering users based on first name, last name, gender, userid or all together. 

* Required APIs have been exposed with documentation.

* Performance analysis is done and report is included. 


# Usage

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.


If you don't have django installed for python 3 then run:

    $ pip3 install django
    
And then:

    $ python3 -m django startproject \
      --template=https://github.com/nikola-k/django-template/zipball/master \
      --extension=py,md \
      <project_name>
      
      
After that just run migrations, and start the server.


# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone sumit-ssr207/crl_assignment.git
    $ cd crl_assignment
    

Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
