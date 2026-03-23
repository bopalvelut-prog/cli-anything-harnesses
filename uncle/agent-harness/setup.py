from setuptools import setup
setup(
    name='cli-anything-uncle',
    version='1.0.0',
    packages=['cli_anything.uncle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-uncle=cli_anything.uncle:cli']},
)
