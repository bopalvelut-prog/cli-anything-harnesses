from setuptools import setup
setup(
    name='cli-anything-leanpub',
    version='1.0.0',
    packages=['cli_anything.leanpub'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-leanpub=cli_anything.leanpub:cli']},
)
