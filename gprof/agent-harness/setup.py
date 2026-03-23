from setuptools import setup
setup(
    name='cli-anything-gprof',
    version='1.0.0',
    packages=['cli_anything.gprof'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gprof=cli_anything.gprof:cli']},
)
