from setuptools import setup
setup(
    name='cli-anything-feel',
    version='1.0.0',
    packages=['cli_anything.feel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-feel=cli_anything.feel:cli']},
)
