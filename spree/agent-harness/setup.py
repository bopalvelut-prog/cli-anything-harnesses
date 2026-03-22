from setuptools import setup
setup(
    name='cli-anything-spree',
    version='1.0.0',
    packages=['cli_anything.spree'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-spree=cli_anything.spree:cli']},
)
