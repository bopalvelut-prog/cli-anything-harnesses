from setuptools import setup
setup(
    name='cli-anything-professor',
    version='1.0.0',
    packages=['cli_anything.professor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-professor=cli_anything.professor:cli']},
)
