from setuptools import setup
setup(
    name='cli-anything-trap',
    version='1.0.0',
    packages=['cli_anything.trap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-trap=cli_anything.trap:cli']},
)
