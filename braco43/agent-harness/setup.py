from setuptools import setup
setup(
    name='cli-anything-braco43',
    version='1.0.0',
    packages=['cli_anything.braco43'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco43=cli_anything.braco43:cli']},
)
