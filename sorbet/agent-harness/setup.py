from setuptools import setup
setup(
    name='cli-anything-sorbet',
    version='1.0.0',
    packages=['cli_anything.sorbet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sorbet=cli_anything.sorbet:cli']},
)
