from setuptools import setup
setup(
    name='cli-anything-mosquitto',
    version='1.0.0',
    packages=['cli_anything.mosquitto'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mosquitto=cli_anything.mosquitto:cli']},
)
