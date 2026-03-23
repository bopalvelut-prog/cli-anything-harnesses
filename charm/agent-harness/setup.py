from setuptools import setup
setup(
    name='cli-anything-charm',
    version='1.0.0',
    packages=['cli_anything.charm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-charm=cli_anything.charm:cli']},
)
