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

Available Endpoints

POST http://localhost:8000/auth/users/ - Signup endpoint

POST http://localhost:8000/auth/token/login - Login endpoint

POST http://localhost:8000/auth/token/logout - Logout endpoint

GET http://localhost:8000/stocks - List of stocks by a user 

POST http://localhost:8000/stocks/{symbol}/buy/{shares}/ - Buy stocks

PUT http://localhost:8000/stocks/{symbol}/sell/{shares}/ - Sell stocks

GET http://localhost:8000/stocks/{symbol}/search/ - Search for a stock

GET http://localhost:8000/transactions/ - List of Transactions

GET http://localhost:8000/transactions/?start_date=YYYYMMDD?end_date=YYYYMMDD/ - Filter List of transactions by date



### Test coverage
To run the tests, check your test coverage, and generate a simplified coverage report:

```python
$ pytest
```

