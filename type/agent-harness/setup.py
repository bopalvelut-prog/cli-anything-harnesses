from setuptools import setup
setup(
    name='cli-anything-type',
    version='1.0.0',
    packages=['cli_anything.type'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-type=cli_anything.type:cli']},
)
