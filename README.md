# 	MoneyManager
### An app from InnovApp

<a href="https://imgbb.com/"><img src="https://i.ibb.co/mXmzxWp/MMLog.png" alt="MMLog" border="0"></a>

## Introduction

This is a WebApp thought to help users with the management of finances. We know that there is a problem, a big problem; we don't have a financial education and that is why we experience failure in the trying of savings. MoneyManager offers you a solution in the financial success,now you can create projects based on a system of categories, track your expenses day by day, month by month and per year having all of your income and expenses controlled. 

Despite the wide range of tools of this type, most of them are full of functionalities that complicate their usage, leaving aside the simple and filling users with information that on a daily basis is not  helpful for users and their goals. Then, the need arises to simplify the personal account management process, which nowadays takes a long time and does not facilitate decision-making due to its complexity to consolidate the information.
With the widespread availability of Git and cloud-computing environments, continuous deployment  means having an arbitrary number of parallel environments, non-linear workflows, and cheap, disposable. There are many possible tools to build a Git-and-Cloud hosting and application deployment workflow. Some are self-hosted while others are a hosted service.. The major drawback of the Git-and-Cloud model is the complexity of the underlying tooling that enables it, and that complexity.



##### Deployed Site

* [MoneyManagerApp](https://herokuapptestuno.herokuapp.com/)


##### Team's LinkedIn

* [Jose Omar](https://www.linkedin.com/in/jose-omar-espinosa-66aa621a1/)
* [Karen](https://www.linkedin.com/in/karen-campo-7862011a1/)
* [Jorge Jhonnyer](https://www.linkedin.com/in/jhonnyer-otalvaro-696b9014b/)


## Desciption 

This project was born in the womb of an academic final project for Holberton School. What seemed to be a race for life has became a method of solving financial problems.
Our product intents to help user with all the  possible finantial aspects, organized into categories. 

### Data Modeling

<a href="https://ibb.co/vw6ZWGw"><img src="https://i.ibb.co/7Yd2D5Y/Data-Modeling.png" alt="Data-Modeling" border="0"></a>

#### Our Entity Relational Model contains:

**1. Table User:**

* id user (Required)
* name user (Required)
* surname user (Required)
* password user (Required)

*The data provided in this table is for the authentication of the system. It is the first part to identify every user of  the platform and the relationship between each function and/or module.*

**2. Table Saving:**

* id saving (Required)
* id user (Required)
* id movement (Required)
* month saving (Required)
* account status (Required)
* account balance (Required)

*Through its primary and foreign keys, obtains the savings, balance and status of each user*.

**3. Table Category:**

* id category (Required)
* name category (Required)
* description category (Required)

*In this table is the categories are created helping the user to know exactly what the savings are focused on.*

**4. Table Budget:**

* id budget (Required)
* id user (Required)
* id category (Required)
* month budget (Required)
* value budget (Required)

*This table contains the required budget information per user; such as the month, the value and the category so can get what they want from the platform.*

**5. Table Movement:**

* id movement (Required)
* id budget (Required)
* month movement (Required)
* value movement (Required)
* description movement (Required)

*Here is where each of the movements made by the user is evidenced, geneting a record the wi saved by the platform.*

## 📋 Folder 

|   **Folder**   |   **Description**   |
| -------------- | --------------------- |
| [app](./app) | The 'app' folder contains the files of the application models and their main configuration. |
| [env](./env) | The env' folder is where the environment variable that executes the application is located.  |
| [requirements ](./requirements) | In the requirements folder there is a txt document with the installations needed to run the application, it is installed through the console by executing 'pip freeze -r requirements.txt'. |


## 🚀 Installation 

* git Clone https://github.com/joer9514/MoneyManagerApp
* Create virtual env with **python -m virtualenv (virtualenv name)**
* Activate virtualenv with *activate*. For windows you must specify the path **env/Scripts/activate**. For Linux the path is **source env/bin/activate**
* Install requirements with **pip install -r requirements/requirements.txt**
* go to the folder **app** with command **cd**
* Run migrations with command **python manage.py makemigrations**
* Run command **python manage.py migrate**
* Now we can run the server for our project with **python manage.py runserver**
* Good to go. Enjoy MoneyManager!

## Usage

[![Watch the video](https://www.youtube.com/watch?v=1fTHCdWwUGI&t=64s)

# ✒️ Authors:
 * Jhonnyer Otalvaro - [Github](https://github.com/Jhonierk) / [Twitter](https://twitter.com/JhonnyerOtalva2)  
 * Karen Campo - [Github](https://github.com/KarenCampo777) / [Twitter](https://twitter.com/KarenCa96752258)  
 * Jose Espinoza - [Github](https://github.com/joer9514) / [Twitter](https://twitter.com/joer9514)  

