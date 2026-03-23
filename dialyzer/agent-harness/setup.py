from setuptools import setup
setup(
    name='cli-anything-dialyzer',
    version='1.0.0',
    packages=['cli_anything.dialyzer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dialyzer=cli_anything.dialyzer:cli']},
)
