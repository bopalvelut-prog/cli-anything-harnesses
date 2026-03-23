from setuptools import setup
setup(
    name='cli-anything-founder',
    version='1.0.0',
    packages=['cli_anything.founder'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-founder=cli_anything.founder:cli']},
)
