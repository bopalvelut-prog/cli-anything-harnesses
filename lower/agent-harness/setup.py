from setuptools import setup
setup(
    name='cli-anything-lower',
    version='1.0.0',
    packages=['cli_anything.lower'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lower=cli_anything.lower:cli']},
)
