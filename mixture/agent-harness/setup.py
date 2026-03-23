from setuptools import setup
setup(
    name='cli-anything-mixture',
    version='1.0.0',
    packages=['cli_anything.mixture'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mixture=cli_anything.mixture:cli']},
)
