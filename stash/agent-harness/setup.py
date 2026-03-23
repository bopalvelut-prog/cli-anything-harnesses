from setuptools import setup
setup(
    name='cli-anything-stash',
    version='1.0.0',
    packages=['cli_anything.stash'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stash=cli_anything.stash:cli']},
)
