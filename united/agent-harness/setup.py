from setuptools import setup
setup(
    name='cli-anything-united',
    version='1.0.0',
    packages=['cli_anything.united'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-united=cli_anything.united:cli']},
)
