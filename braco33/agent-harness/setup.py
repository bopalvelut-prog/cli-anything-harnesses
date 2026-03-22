from setuptools import setup
setup(
    name='cli-anything-braco33',
    version='1.0.0',
    packages=['cli_anything.braco33'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-braco33=cli_anything.braco33:cli']},
)
