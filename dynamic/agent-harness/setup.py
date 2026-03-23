from setuptools import setup
setup(
    name='cli-anything-dynamic',
    version='1.0.0',
    packages=['cli_anything.dynamic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dynamic=cli_anything.dynamic:cli']},
)
