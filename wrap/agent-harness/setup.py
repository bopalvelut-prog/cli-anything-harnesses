from setuptools import setup
setup(
    name='cli-anything-wrap',
    version='1.0.0',
    packages=['cli_anything.wrap'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wrap=cli_anything.wrap:cli']},
)
