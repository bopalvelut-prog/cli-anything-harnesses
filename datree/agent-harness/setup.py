from setuptools import setup
setup(
    name='cli-anything-datree',
    version='1.0.0',
    packages=['cli_anything.datree'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-datree=cli_anything.datree:cli']},
)
