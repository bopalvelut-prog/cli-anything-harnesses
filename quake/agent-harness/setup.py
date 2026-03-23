from setuptools import setup
setup(
    name='cli-anything-quake',
    version='1.0.0',
    packages=['cli_anything.quake'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-quake=cli_anything.quake:cli']},
)
