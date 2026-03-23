from setuptools import setup
setup(
    name='cli-anything-formio',
    version='1.0.0',
    packages=['cli_anything.formio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-formio=cli_anything.formio:cli']},
)
