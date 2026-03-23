from setuptools import setup
setup(
    name='cli-anything-filezilla',
    version='1.0.0',
    packages=['cli_anything.filezilla'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-filezilla=cli_anything.filezilla:cli']},
)
