from setuptools import setup
setup(
    name='cli-anything-barman',
    version='1.0.0',
    packages=['cli_anything.barman'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-barman=cli_anything.barman:cli']},
)
