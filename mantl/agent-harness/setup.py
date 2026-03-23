from setuptools import setup
setup(
    name='cli-anything-mantl',
    version='1.0.0',
    packages=['cli_anything.mantl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mantl=cli_anything.mantl:cli']},
)
