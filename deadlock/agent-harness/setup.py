from setuptools import setup
setup(
    name='cli-anything-deadlock',
    version='1.0.0',
    packages=['cli_anything.deadlock'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-deadlock=cli_anything.deadlock:cli']},
)
