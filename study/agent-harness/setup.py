from setuptools import setup
setup(
    name='cli-anything-study',
    version='1.0.0',
    packages=['cli_anything.study'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-study=cli_anything.study:cli']},
)
