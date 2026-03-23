from setuptools import setup
setup(
    name='cli-anything-weather',
    version='1.0.0',
    packages=['cli_anything.weather'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-weather=cli_anything.weather:cli']},
)
