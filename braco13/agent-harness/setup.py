from setuptools import setup
setup(
    name='cli-anything-braco13',
    version='1.0.0',
    packages=['cli_anything.braco13'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco13=cli_anything.braco13:cli']},
)
