from setuptools import setup
setup(
    name='cli-anything-food',
    version='1.0.0',
    packages=['cli_anything.food'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-food=cli_anything.food:cli']},
)
