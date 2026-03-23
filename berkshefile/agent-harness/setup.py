from setuptools import setup
setup(
    name='cli-anything-berkshefile',
    version='1.0.0',
    packages=['cli_anything.berkshefile'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-berkshefile=cli_anything.berkshefile:cli']},
)
