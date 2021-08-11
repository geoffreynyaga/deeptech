# DeepTech

AI tools for agriculture

## Installation (Linux/WSL)

Install my-project with npm

```bash
  pip install virtualenv
  git clone https://github.com/geoffreynyaga/deeptech.git .
  virtualenv venv
  source venv/bin/activate
  pip install -r requirements.txt
  sudo apt-get install binutils libproj-dev gdal-bin

```

## Setup your postgres database with name  "deeptech" and a password of your choosing
 - NB:  rename .env.sample to .env and prepopulate the database password with the password you created above

```bash
  python manage.py runserver
```
