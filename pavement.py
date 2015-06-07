"""
Paver tasks
"""

from paver.tasks import task, needs
from paver.easy import sh


@task
def week1():
    # Unit tests
    sh('py.test --cov-report term-missing --cov week1/ test/week1/')

    # Syntax validation
    sh('pylint week1/ test/week1/')


@task
def week2():
    # Unit tests
    sh('py.test --cov-report term-missing --cov week2/ test/week2/')

    # Syntax validation
    sh('pylint week2/ test/week2/')


@needs('week1', 'week2')
@task
def default():
    pass
