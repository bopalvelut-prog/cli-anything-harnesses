from setuptools import setup
setup(
    name='cli-anything-bread',
    version='1.0.0',
    packages=['cli_anything.bread'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bread=cli_anything.bread:cli']},
)
