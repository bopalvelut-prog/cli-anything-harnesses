from setuptools import setup
setup(
    name='cli-anything-var',
    version='1.0.0',
    packages=['cli_anything.var'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-var=cli_anything.var:cli']},
)
