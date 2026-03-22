from setuptools import setup
setup(
    name='cli-anything-bun',
    version='1.0.0',
    packages=['cli_anything.bun'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bun=cli_anything.bun:cli']},
)
