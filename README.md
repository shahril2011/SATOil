### What is SATOil?
SATOil or Sentiment Analysis Tool to monitor public opinion about palm Oil is used to analyze the sentiment of text or website article from MPOC to determine the sentiment either it is Positive, Negative, or Neutral. In this sentiment analysis tool, users are able to enter the input as text or enter the website article URL from MPOC to print the output to the users.

# Benefit
1. Able to analyze the sentiment that are input from users.
2. Free to use and easy to use

# Members
1. They are able to choose between text or URL.
2. They are able to view the history of their sentiment analysis activity
3. Print out their analyse to PDF.


# SATOil Project

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

# Additional Commands
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