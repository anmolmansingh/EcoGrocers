# EcoGrocers

## Submission for Visa ClimateTech Hackathon 2024


Running the code on local machine:
--------

Make sure you have django correctly installed by typing in the command:

```
django-admin --version
```
Copy-paste the local env file to the project (it should never be committed)

After creating a virtual environment of your choice, run the requirements.txt file to install your libraries on it
```
pip install -r requirements.txt
```

Next, run the website on local machine by typing the following command in your terminal:

```
python manage.py runserver
```

If you have made changes to the models.py, run:
```
python manaage.py makemigrations
python manage.py migrate
```

