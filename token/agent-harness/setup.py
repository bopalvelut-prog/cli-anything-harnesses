from setuptools import setup
setup(
    name='cli-anything-token',
    version='1.0.0',
    packages=['cli_anything.token'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-token=cli_anything.token:cli']},
)
