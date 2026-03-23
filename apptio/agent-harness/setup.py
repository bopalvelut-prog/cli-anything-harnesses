from setuptools import setup
setup(
    name='cli-anything-apptio',
    version='1.0.0',
    packages=['cli_anything.apptio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-apptio=cli_anything.apptio:cli']},
)
