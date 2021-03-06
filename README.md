
![](https://cheersai.ml/static/img/demo.png)
# Todos

#### Installation
- [x] install ubuntu
- [x] install nginx, mysql, python dev tools
- [x] setup gunicorn
- [x] prepare the server
- [x] get domain
- [x] get certbot
- [x] https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-20-04
- [x] increase upload file size
- [x] include proxy_params; in location of virtual.conf for routing error 


#### Preliminary
- [x] create specification document
- [x] create architecture requirements (ubuntu, nginx, mysql)
- [x] create a mapping plan
- [x] create basic mockups
- [x] Cheers fundus image has text label for left/right eye. Research on how this impacts ML
- [x] If there is an impact, how to get around
- [x] Create flask app
- [x] Create authentication for interface and API
- [x] Create a mechanism to store uploaded files
- [x] Create a mechanism for seemless transitioning when models are updated
- [x] Create table schema
- [x] incorporate datatable
- [x] add email and phone number to patients table
- [x] retrofit the priliminary model
- [x] create a basic home page for portfolio purposes
- [x] research storage for images (local)
- [x] figure out ssh



#### Forms
- [x] create input fields for PATIENT table name, age, gender, address, country, cheersID
- [x] segregate PATIENT with other forms
- [x] create, read, update, delete PATIENT
- [x] create, read, delete USER
- [x] create, read, delete DR
- [x] create, read, delete GLAUCOMA
- [x] Create a page for patient's history
- [x] Separate left and right images
- [x] Login 
- [x] Register

#### QA
- [x] Do not allow bad images (blurry/dark/bright) to be uploaded for prediction
- [x] Identify threshold for prediction (DR)
- [x] Identify threshold for prediction (Glaucoma)

#### Engineering
- [x] Identify patient tracking
- [x] Create a user auth system
- [x] Temporarily deploy on mysql (test) to check if schema match
- [x] Identify other engineering todos

#### Authentication
- [x] use basic auth to create users
- [x] use sessions and email/passwords for users 
- [x] create a flag for admins

#### SCHEMA
- [x] PATIENT
- [x] USER
- [x] DR
- [x] GLAUCOMA


#### User Interface/API
- [x] Create a streamlit app
- [x] Create a demoable app to predict DR
- [x] Add swagger to the project for API documentation
- [x] Add Sphinx for project documentation
- [x] Add bearer authentication for API
- [x] Provide additional information on the interface and not just the prediction (probability, index, charts etc)
- [x] Probability index for Glaucoma (2 levels)
- [x] Use bulma or tailwind for CSS
- [x] add meta tags


# Installation

#### Clone the repository

`https://github.com/ayushsubedi/cheersAI/`


#### CD into the cloned directory and create a virtualenv

`python -m venv env`


### Enable virtualenv

`.\env\Scripts\activate`


### Enable virtualenv (windows)

`.\env\Scripts\activate`

### Install dependency packages from requirements.txt

`pip install -r requirements.txt`

### Run flask app
`source FLASK_APP="app.py"`
`flask run`

### Run flask app (windows)
`$env:FLASK_APP="app.py"`
`flask run`

# Running with docker

```
if __name__ == '__main__':
    application.run(host= '0.0.0.0', debug=True)
```

### Build
```docker build -f Dockerfile -t docker_flask .```

### Run
```docker run -p 5000:5000 -ti docker_flask /bin/bash -c "cd /src && source activate ml && python run.py"```
