from setuptools import setup
setup(
    name='cli-anything-club',
    version='1.0.0',
    packages=['cli_anything.club'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-club=cli_anything.club:cli']},
)
