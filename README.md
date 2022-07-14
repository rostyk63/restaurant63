# restaurant63

## With this app you can:

- ### Change (add / edit / delete) the above data
- ### Create user(login, sign-up)
- ### Create restaurant
- ### See the restaurant's menu for today
- ### Vote for menu

## How to build this project:

- ### Navigate to the project root folder
- ### Activate virtual environment

``` python3 -m venv venv ```

```source venv/bin/activate```

- ### Install the requirements:

```
pip install -r requirements.txt
```

- ### Set the following environment variables:

```
SECRET_KEY=<your_secret_key>

DATABASE_URL=<your_database_url>
```

- ### Configure PostgreSQL database(if you use it)

```
DATABASE_URL=postgres://<your_username>:<your_password>@<your_database_url>/<your_database_name>
```

- ### Run the project locally:

```
python app.py
```

## Now you should be able to access the web application on the following addresses:

```
localhost:5000/

localhost:5000/home
localhost:5000/login
localhost:5000/sign-up
localhost:5000/logout
localhost:5000/restaurant/<int:restaurant_id>
localhost:5000/delete-restaurant/<int:restaurant_id>
localhost:5000/menu-vote
localhost:5000/restaurant/<int:restaurant_id>/menu-vote
localhost:5000/results

