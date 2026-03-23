from setuptools import setup
setup(
    name='cli-anything-arrow',
    version='1.0.0',
    packages=['cli_anything.arrow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-arrow=cli_anything.arrow:cli']},
)
