from setuptools import setup
setup(
    name='cli-anything-zebra',
    version='1.0.0',
    packages=['cli_anything.zebra'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zebra=cli_anything.zebra:cli']},
)
