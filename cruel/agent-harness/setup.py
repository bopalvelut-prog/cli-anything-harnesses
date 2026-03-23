from setuptools import setup
setup(
    name='cli-anything-cruel',
    version='1.0.0',
    packages=['cli_anything.cruel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cruel=cli_anything.cruel:cli']},
)
