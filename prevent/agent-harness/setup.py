from setuptools import setup
setup(
    name='cli-anything-prevent',
    version='1.0.0',
    packages=['cli_anything.prevent'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-prevent=cli_anything.prevent:cli']},
)
