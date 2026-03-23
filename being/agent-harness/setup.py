from setuptools import setup
setup(
    name='cli-anything-being',
    version='1.0.0',
    packages=['cli_anything.being'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-being=cli_anything.being:cli']},
)
