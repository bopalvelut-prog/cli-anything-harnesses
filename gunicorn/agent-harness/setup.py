from setuptools import setup
setup(
    name='cli-anything-gunicorn',
    version='1.0.0',
    packages=['cli_anything.gunicorn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gunicorn=cli_anything.gunicorn:cli']},
)
