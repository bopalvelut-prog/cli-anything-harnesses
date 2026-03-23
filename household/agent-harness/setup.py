from setuptools import setup
setup(
    name='cli-anything-household',
    version='1.0.0',
    packages=['cli_anything.household'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-household=cli_anything.household:cli']},
)
