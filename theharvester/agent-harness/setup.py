from setuptools import setup
setup(
    name='cli-anything-theharvester',
    version='1.0.0',
    packages=['cli_anything.theharvester'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-theharvester=cli_anything.theharvester:cli']},
)
