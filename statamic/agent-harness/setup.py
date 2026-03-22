from setuptools import setup
setup(
    name='cli-anything-statamic',
    version='1.0.0',
    packages=['cli_anything.statamic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-statamic=cli_anything.statamic:cli']},
)
