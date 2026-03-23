from setuptools import setup
setup(
    name='cli-anything-timber',
    version='1.0.0',
    packages=['cli_anything.timber'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-timber=cli_anything.timber:cli']},
)
