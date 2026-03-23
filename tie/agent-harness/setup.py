from setuptools import setup
setup(
    name='cli-anything-tie',
    version='1.0.0',
    packages=['cli_anything.tie'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tie=cli_anything.tie:cli']},
)
