from setuptools import setup
setup(
    name='cli-anything-outside',
    version='1.0.0',
    packages=['cli_anything.outside'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-outside=cli_anything.outside:cli']},
)
