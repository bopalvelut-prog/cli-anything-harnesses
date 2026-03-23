from setuptools import setup
setup(
    name='cli-anything-postman',
    version='1.0.0',
    packages=['cli_anything.postman'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-postman=cli_anything.postman:cli']},
)
