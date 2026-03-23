from setuptools import setup
setup(
    name='cli-anything-terrorist',
    version='1.0.0',
    packages=['cli_anything.terrorist'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-terrorist=cli_anything.terrorist:cli']},
)
