from setuptools import setup
setup(
    name='cli-anything-construct',
    version='1.0.0',
    packages=['cli_anything.construct'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-construct=cli_anything.construct:cli']},
)
