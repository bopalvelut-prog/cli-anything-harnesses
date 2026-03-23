from setuptools import setup
setup(
    name='cli-anything-wednesday',
    version='1.0.0',
    packages=['cli_anything.wednesday'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wednesday=cli_anything.wednesday:cli']},
)
