from setuptools import setup
setup(
    name='cli-anything-greet',
    version='1.0.0',
    packages=['cli_anything.greet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-greet=cli_anything.greet:cli']},
)
