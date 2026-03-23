from setuptools import setup
setup(
    name='cli-anything-selenoid',
    version='1.0.0',
    packages=['cli_anything.selenoid'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-selenoid=cli_anything.selenoid:cli']},
)
