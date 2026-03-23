from setuptools import setup
setup(
    name='cli-anything-summary',
    version='1.0.0',
    packages=['cli_anything.summary'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-summary=cli_anything.summary:cli']},
)
