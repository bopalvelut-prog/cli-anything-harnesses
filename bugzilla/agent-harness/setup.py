from setuptools import setup
setup(
    name='cli-anything-bugzilla',
    version='1.0.0',
    packages=['cli_anything.bugzilla'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bugzilla=cli_anything.bugzilla:cli']},
)
