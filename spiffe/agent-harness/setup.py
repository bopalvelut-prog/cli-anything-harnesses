from setuptools import setup
setup(
    name='cli-anything-spiffe',
    version='1.0.0',
    packages=['cli_anything.spiffe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spiffe=cli_anything.spiffe:cli']},
)
