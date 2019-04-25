# Steganography Web Application

The application allows you to learn about steganography through implementation. It covers most types of steganography (text, image, and audio). The application has authentication and allows users to login and logout. It also allows users to check their history of encryptions done on the app.  


## Getting Started

Clone the repository

### Prerequisites

You will need to install the following dependencies

```
Python 3.5+
Django 2+
Sonic Pi 3+
```

### Installing

The application is written to run on any OS. 

clone the repository.
Run the following commands
```python
# In the repository
cd steg_app

# Then run the server
python manage.py runserver

# If multiple installations of python exist, try
python3 manage.py runserver

```

This will run the Django server and you can access your web app on:

```
http://127.0.0.1:8000/
```

The app is now functional and ready to use!


## Usage

You can now use the app to encrypt or decrypt, text, images, or audio.

The web app is responsive to all device dimensions!

[![Image from Gyazo](https://i.gyazo.com/43cb838fdb3d09416e9e3f0cd8befa59.png)](https://gyazo.com/43cb838fdb3d09416e9e3f0cd8befa59)

## Demonstration

Presented in class

## Notes

- Works by default in windows. For linux, configure the `qjackctl` audio toolkit to allow Sonic Pi.  
- Sonic Pi should be open durnig execution to allow for the notes to translate into music.

## Built With

* [Python](https://www.python.org/) - Written in python
* [Django](https://www.djangoproject.com/) - The python web framework used
* [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/) - The python web framework used
* [SQLite](https://www.sqlite.org/index.html) - The database used

## Contributing

* Sundeep Kakar
* Shahbegh Singh Kalra
* Aghabi Salama

## Authors

* **Sundeep Kakar**


## Acknowledgments

* Thank you, Professor Scott, for the guidance through the process.
