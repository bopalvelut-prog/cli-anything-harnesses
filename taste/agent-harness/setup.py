from setuptools import setup
setup(
    name='cli-anything-taste',
    version='1.0.0',
    packages=['cli_anything.taste'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-taste=cli_anything.taste:cli']},
)
