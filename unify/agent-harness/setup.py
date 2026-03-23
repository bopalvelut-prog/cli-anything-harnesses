from setuptools import setup
setup(
    name='cli-anything-unify',
    version='1.0.0',
    packages=['cli_anything.unify'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unify=cli_anything.unify:cli']},
)
