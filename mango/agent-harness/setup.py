from setuptools import setup
setup(
    name='cli-anything-mango',
    version='1.0.0',
    packages=['cli_anything.mango'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mango=cli_anything.mango:cli']},
)
