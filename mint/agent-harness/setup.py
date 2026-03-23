from setuptools import setup
setup(
    name='cli-anything-mint',
    version='1.0.0',
    packages=['cli_anything.mint'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mint=cli_anything.mint:cli']},
)
