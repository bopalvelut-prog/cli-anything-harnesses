from setuptools import setup
setup(
    name='cli-anything-slate',
    version='1.0.0',
    packages=['cli_anything.slate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-slate=cli_anything.slate:cli']},
)
