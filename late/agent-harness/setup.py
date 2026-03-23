from setuptools import setup
setup(
    name='cli-anything-late',
    version='1.0.0',
    packages=['cli_anything.late'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-late=cli_anything.late:cli']},
)
