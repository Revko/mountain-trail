## Mountain Trail

A Django-based web application to help organize and manage hiking trips in the Carpathians.

## Overview

Mountain Trail is designed to streamline the management of hiking activities. It allows users to register as participants, browse routes and trips, and search for specific options using various filters. Whether you're an adventurer or a trip organizer, this tool simplifies your workflow.


## Check it out!
[Mountain trail project deployed to Render](https://mountain-trail.onrender.com/)

## Features

User registration and authentication  
Trip and route management  
Skill level assignment to participants  
Search functionality by date, name, or participant  
Clean Bootstrap 4 interface with Crispy Forms  

## Prerequisites

Python 3.10+
Django 5.2
pip

## Installation

git clone https://github.com/Revko/mountain-trail
cd mountain-trail
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## Demo

![Website Interface](static/images/demo.jpg)

## Demo Login

You can test the app functionality using the following demo credentials:

**Username:** demo_user  
**Password:** demo_pass123