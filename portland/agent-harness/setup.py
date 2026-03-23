from setuptools import setup
setup(
    name='cli-anything-portland',
    version='1.0.0',
    packages=['cli_anything.portland'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-portland=cli_anything.portland:cli']},
)
