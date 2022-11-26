#we can do this because 'website', due to the addition of __init__.py is now a python package
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)