from setuptools import setup
setup(
    name='cli-anything-archiva',
    version='1.0.0',
    packages=['cli_anything.archiva'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-archiva=cli_anything.archiva:cli']},
)
