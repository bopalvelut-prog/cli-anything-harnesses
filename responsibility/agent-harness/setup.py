from setuptools import setup
setup(
    name='cli-anything-responsibility',
    version='1.0.0',
    packages=['cli_anything.responsibility'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-responsibility=cli_anything.responsibility:cli']},
)
