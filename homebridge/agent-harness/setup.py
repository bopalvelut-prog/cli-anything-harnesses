from setuptools import setup
setup(
    name='cli-anything-homebridge',
    version='1.0.0',
    packages=['cli_anything.homebridge'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-homebridge=cli_anything.homebridge:cli']},
)
