from setuptools import setup
setup(
    name='cli-anything-pleasure',
    version='1.0.0',
    packages=['cli_anything.pleasure'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pleasure=cli_anything.pleasure:cli']},
)
