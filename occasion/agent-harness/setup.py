from setuptools import setup
setup(
    name='cli-anything-occasion',
    version='1.0.0',
    packages=['cli_anything.occasion'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-occasion=cli_anything.occasion:cli']},
)
