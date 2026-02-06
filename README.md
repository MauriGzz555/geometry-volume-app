# Geometry Volume App

## Project Description

This project is a simple Python application that computes the volume of different
three-dimensional geometric objects.

The application supports volume calculations for:
- Box
- Cone
- Cylinder
- Sphere

---

## Project Structure
geometry-volume-app/
│
├── geometry/
│ ├── box.py # Volume calculation for a box
│ ├── cone.py # Volume calculation for a cone
│ ├── cylinder.py # Volume calculation for a cylinder
│ ├── sphere.py # Volume calculation for a sphere
│ └── __init__.py
│
├── tests/
│ ├── test_box.py # Unit tests for box volume
│ ├── test_cone.py # Unit tests for cone volume
│ ├── test_cylinder.py# Unit tests for cylinder volume
│ ├── test_sphere.py # Unit tests for sphere volume
│ └── init.py
│
├── main.py # Main program, allows user to input which object to calculate the volume for, and
|       the input of variables 
├── README.md # Project documentation
└── requirements.txt # Project dependencies