from setuptools import setup
setup(
    name='cli-anything-silverstripe',
    version='1.0.0',
    packages=['cli_anything.silverstripe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-silverstripe=cli_anything.silverstripe:cli']},
)
