from setuptools import setup
setup(
    name='cli-anything-tech',
    version='1.0.0',
    packages=['cli_anything.tech'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tech=cli_anything.tech:cli']},
)
