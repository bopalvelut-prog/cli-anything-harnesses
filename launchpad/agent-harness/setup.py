from setuptools import setup
setup(
    name='cli-anything-launchpad',
    version='1.0.0',
    packages=['cli_anything.launchpad'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-launchpad=cli_anything.launchpad:cli']},
)
