from setuptools import setup
setup(
    name='cli-anything-minor',
    version='1.0.0',
    packages=['cli_anything.minor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-minor=cli_anything.minor:cli']},
)
