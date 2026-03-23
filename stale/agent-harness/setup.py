from setuptools import setup
setup(
    name='cli-anything-stale',
    version='1.0.0',
    packages=['cli_anything.stale'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stale=cli_anything.stale:cli']},
)
