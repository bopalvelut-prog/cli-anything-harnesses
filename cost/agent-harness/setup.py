from setuptools import setup
setup(
    name='cli-anything-cost',
    version='1.0.0',
    packages=['cli_anything.cost'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cost=cli_anything.cost:cli']},
)
