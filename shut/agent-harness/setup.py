from setuptools import setup
setup(
    name='cli-anything-shut',
    version='1.0.0',
    packages=['cli_anything.shut'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shut=cli_anything.shut:cli']},
)
