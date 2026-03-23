from setuptools import setup
setup(
    name='cli-anything-shopping',
    version='1.0.0',
    packages=['cli_anything.shopping'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shopping=cli_anything.shopping:cli']},
)
