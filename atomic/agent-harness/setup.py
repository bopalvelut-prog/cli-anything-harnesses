from setuptools import setup
setup(
    name='cli-anything-atomic',
    version='1.0.0',
    packages=['cli_anything.atomic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-atomic=cli_anything.atomic:cli']},
)
