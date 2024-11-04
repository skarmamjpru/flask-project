# Blogging Application

This is a simple blogging application built with Flask, SQLAlchemy, and Marshmallow. It allows users to create, read, update, and delete blog posts through a RESTful API.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Folder Descriptions](#folder-Descriptions)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
  - [GET All Blogs](#get-all-blogs)
  - [GET Blog Detail](#get-blog-detail)
  - [POST Create Blog](#post-create-blog)
  - [PUT Update Blog](#put-update-blog)
  - [DELETE Blog](#delete-blog)
- [Example Usage](#example-usage)

## Requirements

- Python 3.7 or higher
- Flask
- Flask-SQLAlchemy
- Flask-Marshmallow
- SQLAlchemy
- Marshmallow

## Installation

1. **Download the Project**:

   - Download the project as a ZIP file or clone the repository.
   - If downloaded as a ZIP file, unzip it.

2. **Navigate to the Project Directory:**
   ```bash
   cd 24M0577_lab11
   ```
3. **Install Dependencies**
   - Use pip to install the required packages by running:
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Application**
   - Start the application by executing:
   ```bash
   flask run --port 8000
   ```
   -The application will be accessible at http://localhost:8000.

## Folder Descriptions

- **`app/`**: This is the main application folder containing all the code related to the Flask application. It includes the initialization of the app, configuration settings, route definitions, and model definitions.

- **`__init__.py`**: This file is responsible for creating the Flask application instance and setting up the necessary configurations. It also initializes the database and imports the routes.

- **`config.py`**: Contains configuration classes for the application. Here you can specify database connection strings, debug settings, and other constants.

- **`models.py`**: Defines the data models using SQLAlchemy, representing the structure of the database tables.

- **`routes.py`**: Contains the route handlers for the application, defining the endpoints for various API operations.

- **`instance/`**: This folder is intended for instance-specific files, such as the SQLite database file. This separation allows for easier management of files that may change during runtime.

  - **`your_database.db`**: This file is created when the application runs and stores all the data related to the blog application.

- **`requirements.txt`**: A text file listing all the required Python packages for the project. This file is used to install the dependencies with `pip install -r requirements.txt`.

- **`run.py`**: The main entry point for the application. When you run this file, it starts the Flask development server.

- **`README.md`**: This documentation file provides an overview of the project, installation instructions, and information on how to use the application.

## API Endpoints

1.  **GET All Blogs**
    • Endpoint: /api/blogs/
    • Method: GET
    • Description: Retrieves a list of all blogs.
    ```bash
    {
     "id": 1,
     "title": "Magnetic-Hill",
     "author": "Skarma",
     "content": "A cyclops hill where vehicles defy gravity...",
     "image_url": "https://media1.thrillophilia.com/filestore/552g4i6pn5c2ggzy6ygnapbk23aw_shutterstock_425389177.jpg"
    },
    ...
    ```
2.  **GET Blog Detail**

    • Endpoint: /api/blogs/<int:blog_id>
    • Method: GET
    • Description: Retrieves the details of a specific blog by ID.

    ```bash
    {
     "id": 1,
     "title": "Magnetic-Hill",
     "author": "Skarma",
     "content": "A cyclops hill where vehicles defy gravity...",
     "image_url": "https://media1.thrillophilia.com/filestore/552g4i6pn5c2ggzy6ygnapbk23aw_shutterstock_425389177.jpg"
    }
    ```

3.  **POST Create Blog**
    • Endpoint: /api/blogs/
    • Method: POST
    • Description: Creates a new blog.
    • Input:

    ```bash
    curl -X POST http://localhost:8000/api/blogs/ \

    -H "Content-Type: application/json" \
    -d '{
    "title": "My New Blog",
    "content": "This blog talks about amazing places to visit.",
    "author": "Skarma",
    "image_url": "https://example.com/my-blog-image.jpg"
    }'

    ```

    • Example Output:

    ```bash
    {

     "author": "Skarma",
     "content": "This blog talks about amazing places to visit.",
     "id": 8,
     "image_url": "https://example.com/my-blog-image.jpg",
     "title": "My New Blog"
     }
    ```

4.  **PUT Update Blog**

    • Endpoint: /api/blogs/<int:blog_id>
    • Method: PUT
    • Description: Updates an existing blog by ID.
    • Input:

    ```bash
    curl -X PUT http://localhost:8000/api/blogs/<blog_id> \
    -H "Content-Type: application/json" \
    -d '{
     "title": "Magnetic Hill"
    }'
    ```

    • Output:

    ```bash
    {
    "id": 1,
    "title": "Updated Blog Title",
    "author": "Skarma",
    "content": "A cyclops hill where vehicles defy gravity...",
    "image_url": "https://media1.thrillophilia.com/filestore/552g4i6pn5c2ggzy6ygnapbk23aw_shutterstock_425389177.jpg"
    }
    ```

5.  **DELETE Blog**

    • Endpoint: /api/blogs/<int:blog_id>
    • Method: DELETE
    • Description: Deletes a specific blog by ID.
    • Example Input:

    ```bash
      curl -X DELETE http://localhost:8000/api/blogs/8
    ```

    • Example Output:

    ```bash
    {
    "message": "Blog deleted successfully"
    }
    ```

## Example Usage

-You can test the API endpoints using tools like cURL
