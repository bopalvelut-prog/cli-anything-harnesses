from setuptools import setup
setup(
    name='cli-anything-hit',
    version='1.0.0',
    packages=['cli_anything.hit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hit=cli_anything.hit:cli']},
)
