Django Blog
Django Blog is a simple web application built with Django framework that allows users to read articles, view article details, filter articles by topic, and leave comments on articles.

Table of Contents
Features
Installation
Usage
Endpoints
Contributing
License
Features
List of Articles: View a list of articles available on the blog.
Article Details: Click on an article to view its details including title, content, topic, and comments.
Filter by Topic: Filter articles based on their topic to find relevant content.
User Comments: Engage with articles by leaving comments to share thoughts and feedback.
Installation
To run the Django Blog locally, follow these steps:

1- Clone the repository: git clone <https://github.com/MohammadRezaeian1997/myblog.git>
2- Install dependencies:pip install -r requirements.txt
3- Apply migrations: python manage.py migrate
4- Run the development server: python manage.py runserver
5- Access the blog:Open your web browser and go to http://localhost:8000 to access the Django Blog.
Usage
List of Articles: Navigate to http://localhost:8000/articles/ to view the list of articles available on the blog.
Article Details: Click on an article title to view its details including title, content, topic, and comments.
Filter by Topic: To filter articles by topic, use the URL pattern http://localhost:8000/articles/filter/<topic>/.
Adding Comments: To add a comment to
