from setuptools import setup
setup(
    name='cli-anything-appium',
    version='1.0.0',
    packages=['cli_anything.appium'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-appium=cli_anything.appium:cli']},
)
