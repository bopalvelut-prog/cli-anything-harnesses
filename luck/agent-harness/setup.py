from setuptools import setup
setup(
    name='cli-anything-luck',
    version='1.0.0',
    packages=['cli_anything.luck'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-luck=cli_anything.luck:cli']},
)
