from setuptools import setup
setup(
    name='cli-anything-bench',
    version='1.0.0',
    packages=['cli_anything.bench'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bench=cli_anything.bench:cli']},
)
