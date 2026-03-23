from setuptools import setup
setup(
    name='cli-anything-sarif',
    version='1.0.0',
    packages=['cli_anything.sarif'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sarif=cli_anything.sarif:cli']},
)
