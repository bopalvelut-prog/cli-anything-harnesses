from setuptools import setup
setup(
    name='cli-anything-strange',
    version='1.0.0',
    packages=['cli_anything.strange'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-strange=cli_anything.strange:cli']},
)
