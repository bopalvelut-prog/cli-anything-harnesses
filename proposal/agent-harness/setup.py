from setuptools import setup
setup(
    name='cli-anything-proposal',
    version='1.0.0',
    packages=['cli_anything.proposal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-proposal=cli_anything.proposal:cli']},
)
