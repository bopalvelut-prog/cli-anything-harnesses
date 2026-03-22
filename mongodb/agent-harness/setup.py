from setuptools import setup
setup(
    name='cli-anything-mongodb',
    version='1.0.0',
    packages=['cli_anything.mongodb'],
    install_requires=['click', 'pymongo'],
    entry_points={'console_scripts': ['cli-anything-mongodb=cli_anything.mongodb:cli']},
)
