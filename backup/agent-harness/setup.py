from setuptools import setup
setup(
    name='cli-anything-backup',
    version='1.0.0',
    packages=['cli_anything.backup'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-backup=cli_anything.backup:cli']},
)
