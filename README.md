
# Rasa custom chatbot 

This is a custom chatbot which can play rock, paper or sicciors and can tell weather of an Indian city. This is a cli application and need to run locally. NLP model is all ready trained, u just need to pull and run in u r machine, no need to train the model


## Installation

To run the project install  python 

```bash
  Install Python 3.9
  
```
    
## Run Locally

Clone the project

```bash
  git clone  https://github.com/abhirockraj/RasaPlay-Weather.git

```

Go to the project directory

```bash
  cd RasaPlay-Weather
```

Install dependencies

```bash
  python3 -m venv /path/to/new/virtual/environment
  path\to\venv\Scripts\activate.bat
  pip install -r requirements.txt
```

Start the actions server

```bash
  rasa run actions
```
Open another command promt in same virtual env to use chatbot

```bash
  rasa shell
```
Enjoy the chat bot !!!
