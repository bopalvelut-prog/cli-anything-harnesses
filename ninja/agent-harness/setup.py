from setuptools import setup
setup(
    name='cli-anything-ninja',
    version='1.0.0',
    packages=['cli_anything.ninja'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ninja=cli_anything.ninja:cli']},
)
