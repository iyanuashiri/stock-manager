# stock-manager


Stock manager is an app for managing buying and selling of stocks in the financial markets. 

This project has three basic apps.

* Accounts - User authentication.
  - Registration
  - Login and Logout
* Stocks
  - Buy a stock
  - Sell shares of a stock
  - List all stocks bought by a user
  - Search for a stock
* Transactions
  - List all transactions by a user
  

# Technology Stack

  * Python 3.6x/3.7x
  * Django Web Framework 2.0x and Django REST Framework
  * SQLite
 
### Installation

Clone the repo
```python
$ git clone https://github.com/iyanuashiri/stock-manager.git

$ cd stock-manager
```

Run migrations
```python
$ python manage.py makemigrations

$ python manage.py migrate
```

Run server
```python
$ python manage.py runserver
```
Application URL
http://localhost:8000/

API Documentation link
http://localhost:8000/swagger/

### Test coverage
To run the tests, check your test coverage, and generate a simplified coverage report:

```python
$ pytest
```
To generate an HTML report

```python
$ coverage html
$ open htmlcov/index.html
```
