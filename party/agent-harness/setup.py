from setuptools import setup
setup(
    name='cli-anything-party',
    version='1.0.0',
    packages=['cli_anything.party'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-party=cli_anything.party:cli']},
)
