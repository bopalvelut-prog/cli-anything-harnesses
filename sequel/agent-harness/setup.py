from setuptools import setup
setup(
    name='cli-anything-sequel',
    version='1.0.0',
    packages=['cli_anything.sequel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sequel=cli_anything.sequel:cli']},
)
