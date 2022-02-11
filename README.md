# Leave App


This is a leave request application


## Setting Up the Application Locally

### Clone the Repository

- `git clone git@github.com:TeamoreA/leave_app.git`

### Setup VirtualEnvironment

- Setup Pyhton virtual environment by running `python3 -m venv venv`

- Activate the virtual environment by running `source venv/bin/activate`

### Install Application Dependencies

- Run the following command to install application dependencies `pip install -r requirements.txt`

### Perform Initial Migrations

- To ensure that the database tables are properly configured, run migrations by running `./manage.py migrate` at the root of the project

### Start the Server

- After successfully performing migrations, the server can be started by running `./manage.py runserver` at the root of the project.
- Visit `http://127.0.0.1:8000/leaverequests/` in your browser to view the application.


