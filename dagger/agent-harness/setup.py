from setuptools import setup
setup(
    name='cli-anything-dagger',
    version='1.0.0',
    packages=['cli_anything.dagger'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dagger=cli_anything.dagger:cli']},
)
