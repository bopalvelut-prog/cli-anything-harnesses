from setuptools import setup
setup(
    name='cli-anything-effort',
    version='1.0.0',
    packages=['cli_anything.effort'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-effort=cli_anything.effort:cli']},
)
