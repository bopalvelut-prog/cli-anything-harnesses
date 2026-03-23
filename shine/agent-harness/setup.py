from setuptools import setup
setup(
    name='cli-anything-shine',
    version='1.0.0',
    packages=['cli_anything.shine'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shine=cli_anything.shine:cli']},
)
