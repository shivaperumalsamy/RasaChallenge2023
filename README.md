# Rasa Challenges 2023 - Sample project


## Creating virtual environment in python

Prerequisites: 

Install Anaconda https://docs.anaconda.com/free/anaconda/install/linux/

1. Create a conda virtual environment 

```
$ conda create --name rasa379
```

2. Activate the virtual environment

```
$ conda activate rasa379
```

3. Install supported Python version

```
$ conda install python=3.7.9
```

4. Install the Rasa and dependency packages:

```
$ pip install -r requirements.txt
```

This will install the bot and all of its requirements.

---

**NOTE:**
This bot should be used with python 3.7.

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

### To run in ARM Mac Reference Link: https://forum.rasa.com/t/an-unofficial-guide-to-installing-rasa-on-an-m1-macbook/51342
