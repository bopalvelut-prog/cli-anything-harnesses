from setuptools import setup
setup(
    name='cli-anything-manner',
    version='1.0.0',
    packages=['cli_anything.manner'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-manner=cli_anything.manner:cli']},
)
