# 	MoneyManager
### An app from InnovApp

<a href="https://imgbb.com/"><img src="https://i.ibb.co/mXmzxWp/MMLog.png" alt="MMLog" border="0"></a>


## Desciption 

This project was born in the womb of an academic final project for Holberton School. What seemed to be a race for life has became a method of solving financial problems.
Our product intents to help user with all the  possible finantial aspects, organized into categories. 

### Data Modeling

<a href="https://ibb.co/vw6ZWGw"><img src="https://i.ibb.co/7Yd2D5Y/Data-Modeling.png" alt="Data-Modeling" border="0"></a>

###### Our Entity Relational Model contains:

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


## Installation 

* git Clone
* cd Lading_MoneyManager


# Authors:
 * [Jhonnyer Otalvaro](https://github.com/Jhonierk)
 * [Karen Campo](https://github.com/KarenCampo777)
 * [Jose Espinoza](https://github.com/joer9514)

