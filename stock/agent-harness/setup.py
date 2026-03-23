from setuptools import setup
setup(
    name='cli-anything-stock',
    version='1.0.0',
    packages=['cli_anything.stock'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stock=cli_anything.stock:cli']},
)
