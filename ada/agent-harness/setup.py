from setuptools import setup
setup(
    name='cli-anything-ada',
    version='1.0.0',
    packages=['cli_anything.ada'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ada=cli_anything.ada:cli']},
)
