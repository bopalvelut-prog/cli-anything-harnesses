from setuptools import setup
setup(
    name='cli-anything-vanguard',
    version='1.0.0',
    packages=['cli_anything.vanguard'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vanguard=cli_anything.vanguard:cli']},
)
