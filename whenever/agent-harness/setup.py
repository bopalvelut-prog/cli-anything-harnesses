from setuptools import setup
setup(
    name='cli-anything-whenever',
    version='1.0.0',
    packages=['cli_anything.whenever'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-whenever=cli_anything.whenever:cli']},
)
