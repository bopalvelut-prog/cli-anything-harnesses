from setuptools import setup
setup(
    name='cli-anything-libxml2',
    version='1.0.0',
    packages=['cli_anything.libxml2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-libxml2=cli_anything.libxml2:cli']},
)
