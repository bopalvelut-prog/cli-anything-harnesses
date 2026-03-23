from setuptools import setup
setup(
    name='cli-anything-mqtt',
    version='1.0.0',
    packages=['cli_anything.mqtt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mqtt=cli_anything.mqtt:cli']},
)
