from setuptools import setup
setup(
    name='cli-anything-exim',
    version='1.0.0',
    packages=['cli_anything.exim'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-exim=cli_anything.exim:cli']},
)
