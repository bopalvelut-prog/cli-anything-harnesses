from setuptools import setup
setup(
    name='cli-anything-envelope',
    version='1.0.0',
    packages=['cli_anything.envelope'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-envelope=cli_anything.envelope:cli']},
)
