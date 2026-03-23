from setuptools import setup
setup(
    name='cli-anything-grand_central',
    version='1.0.0',
    packages=['cli_anything.grand_central'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grand_central=cli_anything.grand_central:cli']},
)
