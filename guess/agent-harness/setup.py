from setuptools import setup
setup(
    name='cli-anything-guess',
    version='1.0.0',
    packages=['cli_anything.guess'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-guess=cli_anything.guess:cli']},
)
