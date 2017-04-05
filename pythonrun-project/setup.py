from os.path import join, dirname

from setuptools import setup, find_packages

import pythonrun


setup(
    name='pythonrun-project',
    version=pythonrun.__version__,
    packages=find_packages(),
    long_description=open('README.txt').read(),

    entry_points={
        'console_scripts': [
                'run-pythonproject = pythonrun.core:print_message',
                'math-please = pythonrun.core:obj3.out',
            ]
    },
    test_suite='tests'
)