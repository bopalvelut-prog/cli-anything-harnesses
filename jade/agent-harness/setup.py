from setuptools import setup
setup(
    name='cli-anything-jade',
    version='1.0.0',
    packages=['cli_anything.jade'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jade=cli_anything.jade:cli']},
)
