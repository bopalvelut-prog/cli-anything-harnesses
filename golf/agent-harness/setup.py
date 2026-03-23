from setuptools import setup
setup(
    name='cli-anything-golf',
    version='1.0.0',
    packages=['cli_anything.golf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-golf=cli_anything.golf:cli']},
)
