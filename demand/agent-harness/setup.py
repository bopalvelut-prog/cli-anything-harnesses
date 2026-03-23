from setuptools import setup
setup(
    name='cli-anything-demand',
    version='1.0.0',
    packages=['cli_anything.demand'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-demand=cli_anything.demand:cli']},
)
