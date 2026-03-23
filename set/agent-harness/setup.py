from setuptools import setup
setup(
    name='cli-anything-set',
    version='1.0.0',
    packages=['cli_anything.set'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-set=cli_anything.set:cli']},
)
