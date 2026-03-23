from setuptools import setup
setup(
    name='cli-anything-subtitle',
    version='1.0.0',
    packages=['cli_anything.subtitle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-subtitle=cli_anything.subtitle:cli']},
)
