from setuptools import setup
setup(
    name='cli-anything-wound',
    version='1.0.0',
    packages=['cli_anything.wound'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wound=cli_anything.wound:cli']},
)
