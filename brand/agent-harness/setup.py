from setuptools import setup
setup(
    name='cli-anything-brand',
    version='1.0.0',
    packages=['cli_anything.brand'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-brand=cli_anything.brand:cli']},
)
