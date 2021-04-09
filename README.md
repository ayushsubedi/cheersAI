
![Image of Yaktocat](https://github.com/CHEERS-Hospital/cheersAI/blob/main/cheersAI/static/img/logo.png?raw=true)



# Todos
- [x] create specification document
- [x] create architecture requirements (ubuntu, nginx, mysql)
- [ ] research storage for images
- [ ] create a mapping plan
- [ ] create basic mockups
- [x] Cheers fundus image has text label for left/right eye. Research on how this impacts ML
- [x] If there is an impact, how to get around
- [x] Create flask app
- [x] Create authentication for interface and API
- [x] Create a mechanism to store uploaded files
- [ ] Create a mechanism for seemless transitioning when models are updated
- [ ] Add issue trackers
- [ ] Identify more engineering problems
- [ ] Figure out ways to deploy for staging
- [ ] Create table schema
- [ ] Identify patient tracking
- [ ] Create a simple dashboard 
- [ ] 


#### User Interface/API
- [x] Create a streamlit app
- [x] Create a demoable app to predict DR
- [x] Add swagger to the project for API documentation
- [ ] Add Sphinx for project documentation
- [ ] Add bearer authentication for API
- [ ] Provide additional information on the interface and not just the prediction (probability, index, charts etc)
- [x] Use bulma or tailwind for CSS
- [ ] Identify more UI/API todos

# Mockup
![](https://github.com/CHEERS-Hospital/cheersAI/blob/main/cheersAI/static/img/mockups.png?raw=true)

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
