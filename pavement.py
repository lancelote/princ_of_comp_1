"""
Paver tasks
"""

from paver.tasks import task, needs
from paver.easy import sh


@task
def week1():
    # Unit tests
    sh('py.test --cov-report term-missing --cov week1/ test/week1/')

    # Acceptance tests
    sh('behave test/week1/acceptance/features/')

    # Syntax validation
    sh('pylint week1/ test/week1/')


@needs('week1')
@task
def default():
    pass
