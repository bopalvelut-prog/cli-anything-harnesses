from setuptools import setup
setup(
    name='cli-anything-permit',
    version='1.0.0',
    packages=['cli_anything.permit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-permit=cli_anything.permit:cli']},
)
