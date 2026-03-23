from setuptools import setup
setup(
    name='cli-anything-fresh',
    version='1.0.0',
    packages=['cli_anything.fresh'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fresh=cli_anything.fresh:cli']},
)
