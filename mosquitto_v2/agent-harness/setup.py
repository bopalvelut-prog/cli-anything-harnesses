from setuptools import setup
setup(
    name='cli-anything-mosquitto_v2',
    version='1.0.0',
    packages=['cli_anything.mosquitto_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mosquitto_v2=cli_anything.mosquitto_v2:cli']},
)
