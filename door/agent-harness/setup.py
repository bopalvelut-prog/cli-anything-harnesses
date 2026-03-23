from setuptools import setup
setup(
    name='cli-anything-door',
    version='1.0.0',
    packages=['cli_anything.door'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-door=cli_anything.door:cli']},
)
