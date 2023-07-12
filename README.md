# Rasa Challenges 2023 - Sample project


## Creating virtual environment in python

Prerequisites: 

Install Anaconda https://docs.anaconda.com/free/anaconda/install/linux/

1. Create a conda virtual environment 

```
$ conda create --name rasa
```

2. Activate the virtual environment

```
$ conda activate rasa
```

3. Install supported Python version

```
$ conda install python=3.8
```

4. Upgrade pip

```
$ pip install --upgrade pip
```

5. Install the Rasa and dependency packages:

```
$ pip install -r requirements.txt
```

This will install the bot and all of its requirements.

---

**NOTE:**
This bot should be used with python 3.8.

---

## Running the Chatbot

Use `rasa train` to train a model. The amount of memory consumed depends upon the training data added to the files.

To run the action server open a new terminal window and run the following command:

```
$ rasa run actions
```

To run the Core/NLU server use the following command:

```
$ rasa run --enable-api --cors "*"
```

In order to include environment variables during server startup, user the following commands to start the server:

Action server:

```
$ python -m server run actions
```

Core/NLU server:

```
$ python -m server run --enable-api --cors "*"
```



## Adding training data thru API

1. the APIs endpoints are exposed in app.py

2. run the app.py using `python app.py` and the service will be accessible in `http://localhost:8080/status`

