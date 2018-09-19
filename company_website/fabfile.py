from fabric.api import local
from fabric.decorators import task


@task
def run():
    """Run Django server"""
    local('python manage.py runserver')

@task
def freeze():
    """Collect requirements packages"""
    local('pip freeze > requirements.txt')