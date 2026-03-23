from setuptools import setup
setup(
    name='cli-anything-card',
    version='1.0.0',
    packages=['cli_anything.card'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-card=cli_anything.card:cli']},
)
