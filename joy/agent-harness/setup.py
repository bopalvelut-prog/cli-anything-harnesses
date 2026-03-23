from setuptools import setup
setup(
    name='cli-anything-joy',
    version='1.0.0',
    packages=['cli_anything.joy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-joy=cli_anything.joy:cli']},
)
