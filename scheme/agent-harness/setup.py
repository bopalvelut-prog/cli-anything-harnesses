from setuptools import setup
setup(
    name='cli-anything-scheme',
    version='1.0.0',
    packages=['cli_anything.scheme'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scheme=cli_anything.scheme:cli']},
)
