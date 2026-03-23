from setuptools import setup
setup(
    name='cli-anything-operator',
    version='1.0.0',
    packages=['cli_anything.operator'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-operator=cli_anything.operator:cli']},
)
