from setuptools import setup
setup(
    name='cli-anything-pizza',
    version='1.0.0',
    packages=['cli_anything.pizza'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pizza=cli_anything.pizza:cli']},
)
