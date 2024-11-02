# Project Setup Instructions

1. **Change to project directory:**

   ```bash
   cd 24m0857lab11
   ```

2. **Make sure that you have Flask installed. If not, then run:**

   ```bash
   pip install Flask Flask-SQLAlchemy
   ```

3. **Set Up the Database:**
   The application uses SQLAlchemy for ORM. The database will be created automatically when you run the application for the first time.

   OR

   First, create a Database for fetching blog details. Run:

   ```bash
   python3 data.py
   ```

4. **Run the Flask app:**

   ```bash
   python app.py
   ```

5. **Access the Application:**
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

# Project Structure Overview

1. **Instance:**

   - **site.db:** This is the SQLite database file, which stores all data for the application, including blog posts, comments, etc. The database is managed via SQLAlchemy, Flask’s ORM, allowing for easy interactions with the stored data.

2. **config.py:**

   - This file contains configuration settings for the Flask application, such as the secret key, database URI, and any other configurable options. It separates environment-specific configurations (development, testing, production) to enhance flexibility and security.

3. **data.py:**

   - **data.py:** It is a setup script responsible for initializing the database and inserting any sample data. This script includes code to create all database tables, populate initial data, and define any startup configurations required for a fresh database instance.

4. **templates/ Folder:**
   The templates folder stores all HTML template files used by Flask to render views dynamically. Each HTML file serves as a template for a specific page or feature of the web application.

   - **home.html:** The main homepage template, typically displaying an overview of available blogs and any other introductory content.
   - **blog.html:** A template used to display individual blog posts in detail, including images, text, author information, etc.
   - **contact.html:** A template for the contact page, where users can find ways to reach out or submit inquiries.
   - **account.html:** This template serves as the user account page, allowing users to view or update account details and interact with features relevant to their profile.

5. **static:**
   The static folder holds all the static assets required by the website, such as images, stylesheets, etc.

---

# URLs and Expected Outcomes

| URL                     | Description                                                                                                                                                |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **/**                   | Home page displaying all blogs.                                                                                                                            |
|                         | - A list of all blog posts with titles and images. Each post should have a “Read More” link.                                                               |
| **/account**            | User account page.                                                                                                                                         |
|                         | - Displays user information (e.g., name, bio).                                                                                                             |
| **/contact**            | Contact page.                                                                                                                                              |
|                         | - Displays contact information or a contact form.                                                                                                          |
| **/blog/<int:blog_id>** | Detailed view of a specific blog post.                                                                                                                     |
|                         | - Displays the title, content, author, and image of the selected blog post. If the blog post does not exist, it returns a 404 error with “Blog not found.” |
| **/search**             | Search functionality for blog titles.                                                                                                                      |
|                         | - Displays search results based on the query entered. If no results are found, it should show an empty list or relevant message.                           |
