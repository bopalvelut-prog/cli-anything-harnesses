from setuptools import setup
setup(
    name='cli-anything-legend',
    version='1.0.0',
    packages=['cli_anything.legend'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-legend=cli_anything.legend:cli']},
)
