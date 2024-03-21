# Django Blog

Django Blog is a web application built with Django framework that allows users to read articles, view article details, filter articles by topic, and leave comments on articles.

![Django Blog Demo](demo.gif)

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- **List of Articles**: View a list of articles available on the blog.
- **Article Details**: Click on an article to view its details including title, content, topic, and comments.
- **Filter by Topic**: Filter articles based on their topic to find relevant content.
- **User Comments**: Engage with articles by leaving comments to share thoughts and feedback.

## Installation

To run the Django Blog locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone <https://github.com/MohammadRezaeian1997/myblog.git>
    cd myblog
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Apply migrations**:

    ```bash
    python manage.py migrate
    ```

4. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

5. **Access the blog**:

    Open your web browser and go to `http://localhost:8000` to access the Django Blog.

## Usage

- **List of Articles**: Navigate to `http://localhost:8000/articles/` to view the list of articles available on the blog.
- **Article Details**: Click on an article title to view its details including title, content, topic, and comments.
- **Filter by Topic**: To filter articles by topic, use the URL pattern `http://localhost:8000/articles/filter/<topic>/`.
- **Adding Comments**: To add a comment to an article, send a POST request to `http://localhost:8000/articles/<article_id>/comment/` with the comment text in the request body.

## Endpoints

- **List of Articles**: `/articles/` (GET)
- **Article Details**: `/articles/<article_id>/` (GET)
- **Filter by Topic**: `/articles/filter/<topic>/` (GET)
- **Adding Comments**: `/articles/<article_id>/comment/` (POST)

## Contributing

Contributions to Django Blog are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature`)
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature`)
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

"""
