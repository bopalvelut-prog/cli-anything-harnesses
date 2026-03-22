from setuptools import setup
setup(
    name='cli-anything-borgbackup',
    version='1.0.0',
    packages=['cli_anything.borgbackup'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-borgbackup=cli_anything.borgbackup:cli']},
)
