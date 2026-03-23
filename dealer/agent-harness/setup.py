from setuptools import setup
setup(
    name='cli-anything-dealer',
    version='1.0.0',
    packages=['cli_anything.dealer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dealer=cli_anything.dealer:cli']},
)
