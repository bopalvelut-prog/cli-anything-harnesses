from setuptools import setup
setup(
    name='cli-anything-part',
    version='1.0.0',
    packages=['cli_anything.part'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-part=cli_anything.part:cli']},
)
