from setuptools import setup
setup(
    name='cli-anything-jump',
    version='1.0.0',
    packages=['cli_anything.jump'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jump=cli_anything.jump:cli']},
)
