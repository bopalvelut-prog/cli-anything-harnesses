from setuptools import setup
setup(
    name='cli-anything-pour',
    version='1.0.0',
    packages=['cli_anything.pour'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pour=cli_anything.pour:cli']},
)
