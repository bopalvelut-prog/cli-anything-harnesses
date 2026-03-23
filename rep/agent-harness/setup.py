from setuptools import setup
setup(
    name='cli-anything-rep',
    version='1.0.0',
    packages=['cli_anything.rep'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rep=cli_anything.rep:cli']},
)
