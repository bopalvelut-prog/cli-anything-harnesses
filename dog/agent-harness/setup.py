from setuptools import setup
setup(
    name='cli-anything-dog',
    version='1.0.0',
    packages=['cli_anything.dog'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dog=cli_anything.dog:cli']},
)
