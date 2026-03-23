from setuptools import setup
setup(
    name='cli-anything-awesome',
    version='1.0.0',
    packages=['cli_anything.awesome'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-awesome=cli_anything.awesome:cli']},
)
