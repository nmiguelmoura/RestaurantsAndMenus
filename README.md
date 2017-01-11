# Restaurant Menu Flask App

This app was built as a flask exercise and allows any visitor to get a list of restaurants and respective menus.
Logged users can create, edit and delete restaurants and menus.
The login system uses third-party provides: Google and Facebook.

The project implements a JSON endpoint that serves the same information as displayed in the HTML endpoints for an arbitrary item in the catalog.

Also implements image handling and CSRF to secure form data.

This project was built using Python, Flask and sqlalchemy.

## Run code
The project is configured to run in a Virtualbox VM with Ubuntu, using Vagrant. All the necessary tools, like python, flask and sqlalchemy, oauth2client, requests, httplib2, are already installed in the VM.

To run the code:
- Install [Virtualbox](https://www.virtualbox.org/);

- Install [Vagrant](https://www.vagrantup.com/);

- Fork and clone this repository to your system.

- Through command line, navigate to the project folder and run the code:
`$ vagrant up`

- After that, run:
`$ vagrant ssh`

- Navigate to shared folder vagrant:
`$ cd /vagrant`

- Navigate to folder www:
`$ cd /www`

- Run the file project.py:
`$ python tournament_test.py`

- Test in your browser in port 5000:
`localhost:5000/`