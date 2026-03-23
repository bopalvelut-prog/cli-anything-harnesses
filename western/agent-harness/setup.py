from setuptools import setup
setup(
    name='cli-anything-western',
    version='1.0.0',
    packages=['cli_anything.western'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-western=cli_anything.western:cli']},
)
