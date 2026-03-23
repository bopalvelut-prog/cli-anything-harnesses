from setuptools import setup
setup(
    name='cli-anything-poverty',
    version='1.0.0',
    packages=['cli_anything.poverty'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-poverty=cli_anything.poverty:cli']},
)
