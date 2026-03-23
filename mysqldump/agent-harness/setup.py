from setuptools import setup
setup(
    name='cli-anything-mysqldump',
    version='1.0.0',
    packages=['cli_anything.mysqldump'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mysqldump=cli_anything.mysqldump:cli']},
)
