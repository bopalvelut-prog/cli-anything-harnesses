from setuptools import setup
setup(
    name='cli-anything-scrub',
    version='1.0.0',
    packages=['cli_anything.scrub'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scrub=cli_anything.scrub:cli']},
)
