# IS601 Midterm: Enhanced Calculator

Factory operations, Memento undo/redo, Observer (logging + autosave), pandas CSV persistence, CLI REPL, pytest with >=90% coverage, GitHub Actions.

## Setup
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt

## Run
python -m app

## Commands
add|subtract|multiply|divide|power|root|modulus|int_divide|percent|abs_diff
history | clear | undo | redo | save | load | help | exit

## Tests
pytest --cov=app

## Config (.env)
See .env for directories, precision, autosave, limits.
