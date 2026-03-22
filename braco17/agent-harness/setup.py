from setuptools import setup
setup(
    name='cli-anything-braco17',
    version='1.0.0',
    packages=['cli_anything.braco17'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco17=cli_anything.braco17:cli']},
)
