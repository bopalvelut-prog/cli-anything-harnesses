from setuptools import setup
setup(
    name='cli-anything-education',
    version='1.0.0',
    packages=['cli_anything.education'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-education=cli_anything.education:cli']},
)
