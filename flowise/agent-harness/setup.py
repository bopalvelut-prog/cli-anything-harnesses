from setuptools import setup
setup(
    name='cli-anything-flowise',
    version='1.0.0',
    packages=['cli_anything.flowise'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-flowise=cli_anything.flowise:cli']},
)
