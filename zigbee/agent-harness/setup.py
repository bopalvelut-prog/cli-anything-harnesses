from setuptools import setup
setup(
    name='cli-anything-zigbee',
    version='1.0.0',
    packages=['cli_anything.zigbee'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zigbee=cli_anything.zigbee:cli']},
)
