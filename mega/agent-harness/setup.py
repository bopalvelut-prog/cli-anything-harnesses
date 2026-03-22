from setuptools import setup
setup(
    name='cli-anything-mega',
    version='1.0.0',
    packages=['cli_anything.mega'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mega=cli_anything.mega:cli']},
)
