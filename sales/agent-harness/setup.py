from setuptools import setup
setup(
    name='cli-anything-sales',
    version='1.0.0',
    packages=['cli_anything.sales'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sales=cli_anything.sales:cli']},
)
