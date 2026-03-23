from setuptools import setup
setup(
    name='cli-anything-happy',
    version='1.0.0',
    packages=['cli_anything.happy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-happy=cli_anything.happy:cli']},
)
