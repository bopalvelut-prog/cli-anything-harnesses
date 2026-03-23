from setuptools import setup
setup(
    name='cli-anything-tragedy',
    version='1.0.0',
    packages=['cli_anything.tragedy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tragedy=cli_anything.tragedy:cli']},
)
