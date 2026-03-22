from setuptools import setup
setup(
    name='cli-anything-pipenv',
    version='1.0.0',
    packages=['cli_anything.pipenv'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pipenv=cli_anything.pipenv:cli']},
)
