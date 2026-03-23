from setuptools import setup
setup(
    name='cli-anything-zigbee2mqtt',
    version='1.0.0',
    packages=['cli_anything.zigbee2mqtt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zigbee2mqtt=cli_anything.zigbee2mqtt:cli']},
)
