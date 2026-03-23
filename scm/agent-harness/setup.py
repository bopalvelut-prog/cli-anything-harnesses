from setuptools import setup
setup(
    name='cli-anything-scm',
    version='1.0.0',
    packages=['cli_anything.scm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scm=cli_anything.scm:cli']},
)
