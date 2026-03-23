from setuptools import setup
setup(
    name='cli-anything-river',
    version='1.0.0',
    packages=['cli_anything.river'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-river=cli_anything.river:cli']},
)
