from setuptools import setup
setup(
    name='cli-anything-parallel',
    version='1.0.0',
    packages=['cli_anything.parallel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-parallel=cli_anything.parallel:cli']},
)
