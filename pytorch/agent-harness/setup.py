from setuptools import setup
setup(
    name='cli-anything-pytorch',
    version='1.0.0',
    packages=['cli_anything.pytorch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pytorch=cli_anything.pytorch:cli']},
)
