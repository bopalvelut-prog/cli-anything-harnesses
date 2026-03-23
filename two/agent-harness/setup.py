from setuptools import setup
setup(
    name='cli-anything-two',
    version='1.0.0',
    packages=['cli_anything.two'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-two=cli_anything.two:cli']},
)
