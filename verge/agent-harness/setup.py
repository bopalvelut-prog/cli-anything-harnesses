from setuptools import setup
setup(
    name='cli-anything-verge',
    version='1.0.0',
    packages=['cli_anything.verge'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-verge=cli_anything.verge:cli']},
)
