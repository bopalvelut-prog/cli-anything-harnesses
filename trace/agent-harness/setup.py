from setuptools import setup
setup(
    name='cli-anything-trace',
    version='1.0.0',
    packages=['cli_anything.trace'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-trace=cli_anything.trace:cli']},
)
