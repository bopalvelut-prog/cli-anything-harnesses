from setuptools import setup
setup(
    name='cli-anything-kind',
    version='1.0.0',
    packages=['cli_anything.kind'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kind=cli_anything.kind:cli']},
)
