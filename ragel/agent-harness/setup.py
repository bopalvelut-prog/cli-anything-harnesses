from setuptools import setup
setup(
    name='cli-anything-ragel',
    version='1.0.0',
    packages=['cli_anything.ragel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ragel=cli_anything.ragel:cli']},
)
