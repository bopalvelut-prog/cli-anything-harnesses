from setuptools import setup
setup(
    name='cli-anything-gocd',
    version='1.0.0',
    packages=['cli_anything.gocd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gocd=cli_anything.gocd:cli']},
)
