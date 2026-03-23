from setuptools import setup
setup(
    name='cli-anything-emotion',
    version='1.0.0',
    packages=['cli_anything.emotion'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-emotion=cli_anything.emotion:cli']},
)
