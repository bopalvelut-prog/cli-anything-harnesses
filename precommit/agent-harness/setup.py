from setuptools import setup
setup(
    name='cli-anything-precommit',
    version='1.0.0',
    packages=['cli_anything.precommit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-precommit=cli_anything.precommit:cli']},
)
