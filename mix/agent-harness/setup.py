from setuptools import setup
setup(
    name='cli-anything-mix',
    version='1.0.0',
    packages=['cli_anything.mix'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mix=cli_anything.mix:cli']},
)
