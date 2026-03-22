from setuptools import setup
setup(
    name='cli-anything-customerio',
    version='1.0.0',
    packages=['cli_anything.customerio'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-customerio=cli_anything.customerio:cli']},
)
