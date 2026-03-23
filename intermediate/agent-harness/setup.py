from setuptools import setup
setup(
    name='cli-anything-intermediate',
    version='1.0.0',
    packages=['cli_anything.intermediate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-intermediate=cli_anything.intermediate:cli']},
)
