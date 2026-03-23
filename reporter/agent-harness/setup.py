from setuptools import setup
setup(
    name='cli-anything-reporter',
    version='1.0.0',
    packages=['cli_anything.reporter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reporter=cli_anything.reporter:cli']},
)
