from setuptools import setup
setup(
    name='cli-anything-heroku',
    version='1.0.0',
    packages=['cli_anything.heroku'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-heroku=cli_anything.heroku:cli']},
)
