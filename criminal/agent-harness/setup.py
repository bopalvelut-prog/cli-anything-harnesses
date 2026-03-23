from setuptools import setup
setup(
    name='cli-anything-criminal',
    version='1.0.0',
    packages=['cli_anything.criminal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-criminal=cli_anything.criminal:cli']},
)
