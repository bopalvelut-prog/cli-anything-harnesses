from setuptools import setup
setup(
    name='cli-anything-vacation',
    version='1.0.0',
    packages=['cli_anything.vacation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vacation=cli_anything.vacation:cli']},
)
