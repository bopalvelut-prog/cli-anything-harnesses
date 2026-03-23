from setuptools import setup
setup(
    name='cli-anything-moto',
    version='1.0.0',
    packages=['cli_anything.moto'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-moto=cli_anything.moto:cli']},
)
