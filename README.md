# CRL Assignment

This assignment is deployed on AWS. URL is shared in the email.

The goal of this project is to implement a user listing solution in Django. 

Assignment statement is included on homepage.


![test](https://user-images.githubusercontent.com/112490857/187637501-4fad4bae-b6f8-4fb1-bdd3-e09a06fed2f1.gif)


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
    
Install required library:

    $ pip3 install python-decouple
    

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone sumit-ssr207/crl_assignment.git
    $ cd crl_assignment
    

Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver
    
Server will display URL to connect to:

<img width="547" alt="Screenshot 2022-08-31 at 1 57 38 PM" src="https://user-images.githubusercontent.com/112490857/187632841-36c89a9e-9a79-40cd-8d46-2fead665b5b0.png">

