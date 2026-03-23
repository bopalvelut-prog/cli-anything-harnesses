from setuptools import setup
setup(
    name='cli-anything-byteman',
    version='1.0.0',
    packages=['cli_anything.byteman'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-byteman=cli_anything.byteman:cli']},
)
