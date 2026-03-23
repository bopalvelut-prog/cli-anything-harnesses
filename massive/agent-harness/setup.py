from setuptools import setup
setup(
    name='cli-anything-massive',
    version='1.0.0',
    packages=['cli_anything.massive'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-massive=cli_anything.massive:cli']},
)
