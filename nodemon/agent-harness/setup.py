from setuptools import setup
setup(
    name='cli-anything-nodemon',
    version='1.0.0',
    packages=['cli_anything.nodemon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nodemon=cli_anything.nodemon:cli']},
)
