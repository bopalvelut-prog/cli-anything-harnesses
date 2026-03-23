from setuptools import setup
setup(
    name='cli-anything-newman',
    version='1.0.0',
    packages=['cli_anything.newman'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-newman=cli_anything.newman:cli']},
)
