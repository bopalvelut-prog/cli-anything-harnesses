from setuptools import setup
setup(
    name='cli-anything-plain',
    version='1.0.0',
    packages=['cli_anything.plain'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-plain=cli_anything.plain:cli']},
)
