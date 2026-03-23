from setuptools import setup
setup(
    name='cli-anything-iis',
    version='1.0.0',
    packages=['cli_anything.iis'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-iis=cli_anything.iis:cli']},
)
