from setuptools import setup
setup(
    name='cli-anything-miller',
    version='1.0.0',
    packages=['cli_anything.miller'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-miller=cli_anything.miller:cli']},
)
