from setuptools import setup
setup(
    name='cli-anything-tensorflow',
    version='1.0.0',
    packages=['cli_anything.tensorflow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tensorflow=cli_anything.tensorflow:cli']},
)
