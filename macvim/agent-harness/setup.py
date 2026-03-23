from setuptools import setup
setup(
    name='cli-anything-macvim',
    version='1.0.0',
    packages=['cli_anything.macvim'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-macvim=cli_anything.macvim:cli']},
)
