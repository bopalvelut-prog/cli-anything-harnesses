from setuptools import setup
setup(
    name='cli-anything-beef',
    version='1.0.0',
    packages=['cli_anything.beef'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-beef=cli_anything.beef:cli']},
)
