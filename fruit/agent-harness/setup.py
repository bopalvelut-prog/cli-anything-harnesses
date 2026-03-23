from setuptools import setup
setup(
    name='cli-anything-fruit',
    version='1.0.0',
    packages=['cli_anything.fruit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fruit=cli_anything.fruit:cli']},
)
