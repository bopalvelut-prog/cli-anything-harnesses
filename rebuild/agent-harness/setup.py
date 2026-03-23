from setuptools import setup
setup(
    name='cli-anything-rebuild',
    version='1.0.0',
    packages=['cli_anything.rebuild'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rebuild=cli_anything.rebuild:cli']},
)
