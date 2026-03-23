from setuptools import setup
setup(
    name='cli-anything-concept',
    version='1.0.0',
    packages=['cli_anything.concept'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-concept=cli_anything.concept:cli']},
)
