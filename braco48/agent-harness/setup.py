from setuptools import setup
setup(
    name='cli-anything-braco48',
    version='1.0.0',
    packages=['cli_anything.braco48'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco48=cli_anything.braco48:cli']},
)
