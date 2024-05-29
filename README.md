### Welcome to SATOil, where we can analyze the sentiment of palm oil post using the link of the post. The post will be processed and bring out the output of the sentiment.


# Django Project

This guide provides step-by-step instructions to set up and run a Django project using `pipenv` after cloning it from a repository.

## Prerequisites

Make sure you have the following installed on your system:

- Python (3.x recommended)
- Git
- pip (Python package installer)
- pipenv (can be installed via pip)

## Steps to Set Up the Project
1. Clone the Repository
2. Install pipenv
`pip install pipenv`

3. Install Project Dependencies
If Pipfile is present:
If the repository contains a Pipfile, you can create the virtual environment and install dependencies using:


`pipenv install`
If only requirements.txt is present:
If there is no Pipfile but there is a requirements.txt file, you can install the dependencies with:

`pipenv install -r requirements.txt`

4. Activate the Virtual Environment
Activate the virtual environment created by pipenv:


`pipenv shell`

5. Apply Migrations
Apply the database migrations to set up your database schema:



`python manage.py migrate`

6. Run the Development Server
Start the Django development server:


`python manage.py runserver`
Your Django project should now be up and running. Open your browser and navigate to http://127.0.0.1:8000/ to see your project.

Additional Commands
To deactivate the virtual environment:

`exit`
To install a new package and add it to Pipfile:

`pipenv install package_name`
To uninstall a package and remove it from Pipfile:


`pipenv uninstall package_name`

## Troubleshooting
If you encounter any issues, ensure that all dependencies are correctly listed in the Pipfile or requirements.txt, and that you are using compatible versions of Python and Django.

For further assistance, refer to the Django documentation or the pipenv documentation.

Contact
If you have any questions or issues, please contact [shahril5822@gmail.com].


## To save the requirement.txt file
pipenv requirements > requirements.txt