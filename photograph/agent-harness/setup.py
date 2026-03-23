from setuptools import setup
setup(
    name='cli-anything-photograph',
    version='1.0.0',
    packages=['cli_anything.photograph'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-photograph=cli_anything.photograph:cli']},
)
