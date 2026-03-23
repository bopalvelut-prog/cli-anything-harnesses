from setuptools import setup
setup(
    name='cli-anything-tree',
    version='1.0.0',
    packages=['cli_anything.tree'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tree=cli_anything.tree:cli']},
)
