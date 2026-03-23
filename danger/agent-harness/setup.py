from setuptools import setup
setup(
    name='cli-anything-danger',
    version='1.0.0',
    packages=['cli_anything.danger'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-danger=cli_anything.danger:cli']},
)
