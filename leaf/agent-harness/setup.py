from setuptools import setup
setup(
    name='cli-anything-leaf',
    version='1.0.0',
    packages=['cli_anything.leaf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-leaf=cli_anything.leaf:cli']},
)
