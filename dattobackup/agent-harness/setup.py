from setuptools import setup
setup(
    name='cli-anything-dattobackup',
    version='1.0.0',
    packages=['cli_anything.dattobackup'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dattobackup=cli_anything.dattobackup:cli']},
)
