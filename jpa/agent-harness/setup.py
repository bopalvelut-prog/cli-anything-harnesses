from setuptools import setup
setup(
    name='cli-anything-jpa',
    version='1.0.0',
    packages=['cli_anything.jpa'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jpa=cli_anything.jpa:cli']},
)
