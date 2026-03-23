from setuptools import setup
setup(
    name='cli-anything-buck2',
    version='1.0.0',
    packages=['cli_anything.buck2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-buck2=cli_anything.buck2:cli']},
)
