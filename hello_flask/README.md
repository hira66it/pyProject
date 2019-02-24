# pyProject
python Project

### useful site
[python abstract](http://book.pythontips.com/en/latest/classes.html)

# Flask Tutorial
(VsCode_Flask_Tutorial)[https://code.visualstudio.com/docs/python/tutorial-flask]

## 1. Create virtual env
```console
python3 -m venv <desired_name=env>
```
if it fails for you in:
```console
virtualenv -p python3 <desired_path>
```
Try:
```console
python3 -m virtualenv <desired_path>
```
## 2. Run Flask
```console
python3 -m flask run
python3 -m flask run --host=127.0.0.1 --port=8080
```
## 2. Make requirements
* To make current environment to requirements.txt
```console
Ctrl + Shift + ` : to Open a currently used terminal
pip freeze > requirements.txt
```
* To use in another environment
```console
pip install -r requirements.txt
```
## 3. Debuging
* F9 = BreakPoint
* F10 = Next
* F5 = Start/Stop