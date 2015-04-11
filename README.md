# SongRecommend

Install virtualenv
```
$ pip install virtualenv
```
Create `env` directory
```
$ virtualenv env
```
Install requirements
```
$ env/bin/pip install -r requirements.txt
```
Activate `virtualenv`
```
$ source env/bin/activate
```
Run the server (with virtualenv running)
```
(venv)$ python server.py
```
The server will be running on `http://0.0.0.0:8080/`