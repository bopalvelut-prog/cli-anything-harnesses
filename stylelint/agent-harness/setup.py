from setuptools import setup
setup(
    name='cli-anything-stylelint',
    version='1.0.0',
    packages=['cli_anything.stylelint'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stylelint=cli_anything.stylelint:cli']},
)
