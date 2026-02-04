# TheCharlesProject
This is a project dedicated to Charles

# Setup the server
We'll be using Flask. Documentation: https://flask.palletsprojects.com/en/stable/ Read them, know them, love them. Probably not right away, get situated first, but there will be a quiz. (It actually is pretty decent. some docs are less than useful, and some are longer than wikipedia. but these are good.)

## Prerequisites 

Instructions will be for Windows, I know I hate it too.

From PowerShell, install Python 3.11 via winget (requires Microsoft Store acceptance)
```powershell
winget install --id Python.Python.3.11 -e --accept-package-agreements --accept-source-agreements
```

Verify the install:
```powershell
py -3.11 --version
```

From admin PowerShell run: 
```powershell
Set-ExecutionPolicy RemoteSigned
```
tell it "y" for yes when it asks some rando question.


## First time setup

### Create a Python 3.11 virtual environment
This is to keep different python packages installed for a project without having them interfere with other projects. You might want different versions of a package or whatever. this keeps them separate. don't question it. or do. either way.
```powershell
py -3.11 -m venv venv
```
That created a folder named ```venv``` that will store the details of the python environment.

verify:
```powershell
.\venv\Scripts\python --version
```


### Activate the environment
```powershell
.\venv\Scripts\Activate
```
you should see `(venv)` on your terminal prompt. This indicates that your prompt is using this environment. 

### Upgrade pip and install project requirements
pip manages packages
```powershell
python -m pip install --upgrade pip
```

python uses requirements.txt as list of all packages required for the application. Whenever new packages are added, they will be added here, and this command will need to be re-ran before running the server.
```powershell
pip install -r requirements.txt
```

## Runing the server
```powershell
python app.py
```

### Open the server
Then open http://127.0.0.1:5000 in your browser.

```127.0.0.1``` is the loopback address on a computer. Every computer will send requests off down the network line to be delt with, but if you use ```127.0.0.1``` or ```localhost```(essentially the same thing) it will keep the request local to your machine, allowing for local development.

# development
Flask uses templates. It's basically inserting python into HTML. Templates do not need to have python in it. It's just HTML until we want to add some logic to it. 

```static\``` is where images, css, js and what not will go. 
