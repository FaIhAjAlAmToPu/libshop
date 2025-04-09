# Library Shop

The **Library Shop** is a web application where users can borrow and buy books from libraries registered on the website.

## Features
- Browse books available for borrowing or purchase.
- Register and manage library accounts.
- User-friendly interface for searching and filtering books.
- Secure user authentication and authorization.

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: Django Templates (HTML, CSS, JavaScript)
- **Database**: MySQL

## Installation
1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```bash
    cd library_shop
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Configure the database in `settings.py`.
5. Apply migrations:
    ```bash
    python manage.py migrate
    ```
6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage
- Access the application at `http://127.0.0.1:8000/`.
- Register or log in to start borrowing or buying books.

## License
This project is licensed under the MIT License.