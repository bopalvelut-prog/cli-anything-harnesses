from setuptools import setup
setup(
    name='cli-anything-primitives',
    version='1.0.0',
    packages=['cli_anything.primitives'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-primitives=cli_anything.primitives:cli']},
)
