from setuptools import setup
setup(
    name='cli-anything-representative',
    version='1.0.0',
    packages=['cli_anything.representative'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-representative=cli_anything.representative:cli']},
)
