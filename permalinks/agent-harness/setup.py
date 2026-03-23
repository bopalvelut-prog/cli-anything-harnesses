from setuptools import setup
setup(
    name='cli-anything-permalinks',
    version='1.0.0',
    packages=['cli_anything.permalinks'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-permalinks=cli_anything.permalinks:cli']},
)
