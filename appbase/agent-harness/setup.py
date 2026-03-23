from setuptools import setup
setup(
    name='cli-anything-appbase',
    version='1.0.0',
    packages=['cli_anything.appbase'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-appbase=cli_anything.appbase:cli']},
)
