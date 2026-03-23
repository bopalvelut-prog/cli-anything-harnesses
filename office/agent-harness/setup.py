from setuptools import setup
setup(
    name='cli-anything-office',
    version='1.0.0',
    packages=['cli_anything.office'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-office=cli_anything.office:cli']},
)
