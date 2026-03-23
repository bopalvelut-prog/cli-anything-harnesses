from setuptools import setup
setup(
    name='cli-anything-blast',
    version='1.0.0',
    packages=['cli_anything.blast'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-blast=cli_anything.blast:cli']},
)
