from setuptools import setup
setup(
    name='cli-anything-innodb',
    version='1.0.0',
    packages=['cli_anything.innodb'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-innodb=cli_anything.innodb:cli']},
)
