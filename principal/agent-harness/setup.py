from setuptools import setup
setup(
    name='cli-anything-principal',
    version='1.0.0',
    packages=['cli_anything.principal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-principal=cli_anything.principal:cli']},
)
