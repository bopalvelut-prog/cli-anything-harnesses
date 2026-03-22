from setuptools import setup
setup(
    name='cli-anything-botkube',
    version='1.0.0',
    packages=['cli_anything.botkube'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-botkube=cli_anything.botkube:cli']},
)
