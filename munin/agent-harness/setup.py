from setuptools import setup
setup(
    name='cli-anything-munin',
    version='1.0.0',
    packages=['cli_anything.munin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-munin=cli_anything.munin:cli']},
)
