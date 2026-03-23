from setuptools import setup
setup(
    name='cli-anything-propagation',
    version='1.0.0',
    packages=['cli_anything.propagation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-propagation=cli_anything.propagation:cli']},
)
