from setuptools import setup
setup(
    name='cli-anything-pprof',
    version='1.0.0',
    packages=['cli_anything.pprof'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pprof=cli_anything.pprof:cli']},
)
