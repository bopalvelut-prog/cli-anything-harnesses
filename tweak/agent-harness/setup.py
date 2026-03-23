from setuptools import setup
setup(
    name='cli-anything-tweak',
    version='1.0.0',
    packages=['cli_anything.tweak'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tweak=cli_anything.tweak:cli']},
)
