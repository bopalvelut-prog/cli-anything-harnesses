from setuptools import setup
setup(
    name='cli-anything-sun',
    version='1.0.0',
    packages=['cli_anything.sun'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sun=cli_anything.sun:cli']},
)
