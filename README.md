# Ishu Dawati

A simple [Issue Tracking](./) Management System that support Ticket System. The app allows users to raise an issue and track if it has resolved or not.

[Live Demo](./)

## Table of Content

- [Issue Tracking Management System](#issue-tracking-management-system)
  - [Table of Content](#table-of-content)
    - [How to run](#how-to-run)
    - [Features](#features)
    - [Screenshot](#screenshot)

### How to run

- Create a virtual environment

  ```sh
  > python -m venv .venv
  ```

- Activate it

  ```sh
  > source .venv/bin/activate
  ```

- Install packages

  ```sh
  > pip install -r requirements.txt
  ```

- Start development server

  ```sh
  > python manage.py runserver
  ```

### Features

**Admin Portal**:

**User Portal**:

- ❌ A user should be able to login to his/her account
- If authenticated,
  - ❌ A user should be able to view all the tickets he/she has submitted
  - ❌ A user should be able to search a ticket by keyword
  - ❌ A user should be able to filter and sort tickets based on their preferences
  - ❌ A user should be able to view details on specific ticket
  - ❌ A user should be able to add comment to a specific ticket

### Screenshot

1. **User Registration page**

   ![User Registration page](./screenshots/signup-form.png)

2. **User Login Page**

   ![User Login Page](./screenshots/signin-form.png)

3. **View All Ticket**

   ![View All Ticket page](./)

4. **View Ticket Detail**

   ![View Ticket Detail page](./)

5. **Submit Ticket Through Portal**

   ![Create New Ticket page](./)

6. **Add Comment**
   ![Create New Ticket page](./)
