from setuptools import setup
setup(
    name='cli-anything-polymer',
    version='1.0.0',
    packages=['cli_anything.polymer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-polymer=cli_anything.polymer:cli']},
)
