from setuptools import setup
setup(
    name='cli-anything-activegraph',
    version='1.0.0',
    packages=['cli_anything.activegraph'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-activegraph=cli_anything.activegraph:cli']},
)
