from setuptools import setup
setup(
    name='cli-anything-applesilicon',
    version='1.0.0',
    packages=['cli_anything.applesilicon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-applesilicon=cli_anything.applesilicon:cli']},
)
