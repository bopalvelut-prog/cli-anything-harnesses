from setuptools import setup
setup(
    name='cli-anything-outlook',
    version='1.0.0',
    packages=['cli_anything.outlook'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-outlook=cli_anything.outlook:cli']},
)
