from setuptools import setup
setup(
    name='cli-anything-warehouse',
    version='1.0.0',
    packages=['cli_anything.warehouse'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-warehouse=cli_anything.warehouse:cli']},
)
