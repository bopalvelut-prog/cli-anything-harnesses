from setuptools import setup
setup(
    name='cli-anything-nswag',
    version='1.0.0',
    packages=['cli_anything.nswag'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nswag=cli_anything.nswag:cli']},
)
