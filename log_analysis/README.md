****************** LOG ANALYSIS PROJECT ***********************

Aim of the Program :
For this project, my task was to create a reporting tool that prints out reports( in plain text) based on the data in the given database. This reporting tool is a Python program using the `psycopg2` module to connect to the database. This project sets up a mock PostgreSQL database for a fictional news website. The provided Python script uses the psycopg2 library to query the database and produce a report that answers the following three questions:

    1. To find out the most popular 3 articles.
    2. To find out which authors get the most page views on their articles.
    3. Days on which there were more than 1% requests that led to errors.

Requirements:
    1. Download vagrant.
        You can download it from vagrantup.com .
    2. Download VirtualBox.
        You can download it from virtualbox.org.
    3. Download VM Configuration.
        You can fork and clone it from
        https://github.com/udacity/fullstack-nanodegree-vm . 
        
How to run the Program :
    1. Download database(zip) on which operations are to be performed.
    2. Extract the file in vagrant directory.
    3. Download the project.
    4. Extract all files in vagrant directory.
    5. Open terminal in your system.
    6. Change the path to vagrant.
    7. Use "vagrant up" command to setup Virtual Machine.
    8. Use "vagrant ssh" to login.
    9. Change path to /vagrant/Project.
   10. Run psql -d NEWS -f newsdata.sql for loading the data.
   11. Now simply run the command "python log.py".
