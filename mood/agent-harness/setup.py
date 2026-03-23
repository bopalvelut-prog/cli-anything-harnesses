from setuptools import setup
setup(
    name='cli-anything-mood',
    version='1.0.0',
    packages=['cli_anything.mood'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mood=cli_anything.mood:cli']},
)
