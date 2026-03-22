from setuptools import setup
setup(
    name='cli-anything-mysql',
    version='1.0.0',
    packages=['cli_anything.mysql'],
    install_requires=['click', 'mysql-connector-python'],
    entry_points={'console_scripts': ['cli-anything-mysql=cli_anything.mysql:cli']},
)
