from setuptools import setup
setup(
    name='cli-anything-agola',
    version='1.0.0',
    packages=['cli_anything.agola'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-agola=cli_anything.agola:cli']},
)
