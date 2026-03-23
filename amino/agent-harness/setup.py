from setuptools import setup
setup(
    name='cli-anything-amino',
    version='1.0.0',
    packages=['cli_anything.amino'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-amino=cli_anything.amino:cli']},
)
