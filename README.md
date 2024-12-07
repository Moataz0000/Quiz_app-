# Quiz App API 

## Overview

This is a Django-based API for managing a quiz app. It includes functionalities to manage questions and answers and to check if the user's selected answer is correct. The app allows admins to create, read, update, and delete questions and answers, providing an endpoint for users to submit answers and verify their correctness.


![Quiz_Service](https://github.com/user-attachments/assets/4b478a75-ddf0-4d35-acf1-5fa7a8dd37fe)





## Table of Contents
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
  - [Question Endpoints](#question-endpoints)
  - [Answer Endpoints](#answer-endpoints)
  - [Check Answer Endpoint](#check-answer-endpoint)


## Installation

### Prerequisites

Make sure you have the following installed:
- Python 3.10
- Django 5
- Django REST Framework

### Backend Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/Moataz0000/Quiz_app-.git
    cd core
    ```

2. Set up a virtual environment:

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser for admin access:

    ```bash
    python manage.py createsuperuser
    ```

6. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### Question Endpoints Example 

- **GET /api/questions/**  
  Fetch all available questions.

  **Response:**
  ```json
   [
    {
      "uuid": "uuid-value",
      "question": "What is Django?",
      "created": "2024-12-01T12:00:00Z",
      "available": true
      "answers": [
            {
                "answer": "no thing",
                "is_correct": false,
                "uuid": "253540b1-f2ab-4fce-b832-01f7db24d3ea",
                "created": "2024-12-07T14:02:03.321170Z"
            },
            {
                "answer": "no thing",
                "is_correct": false,
                "uuid": "f7f03ba7-0494-454e-a391-b6e4ecd166af",
                "created": "2024-12-07T14:01:57.521264Z"
            },
            {
                "answer": "no thing",
                "is_correct": false,
                "uuid": "dda8cfed-737d-4c52-b031-5a413ddf9d46",
                "created": "2024-12-07T14:01:52.406848Z"
            },
            {
                "answer": "Django is a web framework for Python.",
                "is_correct": true,
                "uuid": "2ca812f1-03d0-4beb-9bbe-3829926f118e",
                "created": "2024-12-07T14:01:36.220961Z"
            }
    },



   
