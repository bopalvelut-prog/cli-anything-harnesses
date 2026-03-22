from setuptools import setup
setup(
    name='cli-anything-shiden',
    version='1.0.0',
    packages=['cli_anything.shiden'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shiden=cli_anything.shiden:cli']},
)
