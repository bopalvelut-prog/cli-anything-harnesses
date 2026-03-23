from setuptools import setup
setup(
    name='cli-anything-riot',
    version='1.0.0',
    packages=['cli_anything.riot'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-riot=cli_anything.riot:cli']},
)
