from setuptools import setup
setup(
    name='cli-anything-picard',
    version='1.0.0',
    packages=['cli_anything.picard'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-picard=cli_anything.picard:cli']},
)
