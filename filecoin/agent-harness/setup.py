from setuptools import setup
setup(
    name='cli-anything-filecoin',
    version='1.0.0',
    packages=['cli_anything.filecoin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-filecoin=cli_anything.filecoin:cli']},
)
