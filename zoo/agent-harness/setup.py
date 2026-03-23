from setuptools import setup
setup(
    name='cli-anything-zoo',
    version='1.0.0',
    packages=['cli_anything.zoo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zoo=cli_anything.zoo:cli']},
)
