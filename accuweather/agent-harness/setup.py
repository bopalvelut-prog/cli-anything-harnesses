from setuptools import setup
setup(
    name='cli-anything-accuweather',
    version='1.0.0',
    packages=['cli_anything.accuweather'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-accuweather=cli_anything.accuweather:cli']},
)
