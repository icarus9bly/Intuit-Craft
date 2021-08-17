# snake-and-ladder-python

Multi user snakes and ladders games

# Installation

### Dependencies

- `Python 3.8.8`
- `termcolor 1.1.0`
- `colorama 0.4.4`

### Setup

1. Install `Python 3.8.8`

2. Install and activate the virtual environment
```
cd <project_dir>/
pip -m venv .
```

If you haven't already, clone this project from your fork, and enter the main directory.

```
# on linux/macOS
source /bin/activate
# on windows
bin\activate
```

Your command prompt should look something like this -

```
(env) $ 
```

3. Install all dependencies

```
pip install -r requirements.txt
```

In the event you want to add a dependency, make sure to `pip install` it only when the virtualenv is active. Once that is done, run the following command to add your dependency to `requirements.txt` -
```
pip freeze > requirements.txt
```

3. Run it

```
(env) $ python manage.py runserver
```

# Rules

1. After running the game, the you'll be asked about the number of users ranging from 1 and 4 

2. The grid gets loaded with user's beed at the start position

3. Press <kbd>roll</kbd> to roll the dice.

4. With each roll the grid gets updated with an updated score the goal.

5. The first person to reach the end will be declared as a winner

# TBD
- Add css grid
- Reshuffle Snakes and Ladders
- Mail notification via kafka through mail server
- Interactive edit mode in grid
