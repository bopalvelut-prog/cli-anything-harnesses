from setuptools import setup
setup(
    name='cli-anything-rhel',
    version='1.0.0',
    packages=['cli_anything.rhel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rhel=cli_anything.rhel:cli']},
)
