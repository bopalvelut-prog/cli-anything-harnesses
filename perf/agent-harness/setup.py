from setuptools import setup
setup(
    name='cli-anything-perf',
    version='1.0.0',
    packages=['cli_anything.perf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-perf=cli_anything.perf:cli']},
)
