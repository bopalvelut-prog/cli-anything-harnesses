from setuptools import setup
setup(
    name='cli-anything-handle',
    version='1.0.0',
    packages=['cli_anything.handle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-handle=cli_anything.handle:cli']},
)
