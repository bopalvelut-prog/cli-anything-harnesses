from setuptools import setup
setup(
    name='cli-anything-desk',
    version='1.0.0',
    packages=['cli_anything.desk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-desk=cli_anything.desk:cli']},
)
