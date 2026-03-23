from setuptools import setup
setup(
    name='cli-anything-stagger',
    version='1.0.0',
    packages=['cli_anything.stagger'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stagger=cli_anything.stagger:cli']},
)
