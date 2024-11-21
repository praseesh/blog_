# Blog Platform

## Overview

The Blog Platform is a web application that provides features for managing blog posts, user authentication, and interaction through comments and likes. Built using Django REST Framework, this project allows users to register, log in, create, edit, and delete blog posts, as well as interact with posts by liking and commenting. The application uses JWT authentication to securely handle user sessions and access.

## Features

- **User Authentication**: Register, login, and manage user profiles using JWT authentication.
- **Post Management**: Create, read, update, and delete blog posts.
- **Likes**: Users can like posts, and the like count is updated accordingly.
- **Comments**: Users can comment on posts, facilitating interaction.
- **Role-based Access**: Different levels of access for users (e.g., admin can manage posts and comments, regular users can only interact with posts).
- **JWT Authentication**: Secure and token-based authentication for user sessions.

## Technologies Used

- **Python**
- **Django**
- **Django REST Framework**
- **Simple JWT** (for JWT authentication)
- **PostgreSQL** (for database management)

## Installation

### Prerequisites

- Python 3.8 or higher
- PostgreSQL (or any preferred database system)
- Virtual environment (recommended)

### Steps to run the project

1. Clone the repository:

   ```bash
   git clone https://github.com/praseesh/blog_platform.git

2. Navigate to the project directory:
   ```bash
   cd blog_platform

3. Create and activate a virtual environment:
   
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows: venv\Scripts\activate
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

6. Set up the database:
   ```bash
   python manage.py migrate

7. Run the development server:
   ```bash
   python manage.py runserver

The API will be available at:
  ```bash
  http://127.0.0.1:8000/
