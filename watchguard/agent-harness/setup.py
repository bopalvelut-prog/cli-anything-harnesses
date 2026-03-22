from setuptools import setup
setup(
    name='cli-anything-watchguard',
    version='1.0.0',
    packages=['cli_anything.watchguard'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-watchguard=cli_anything.watchguard:cli']},
)
