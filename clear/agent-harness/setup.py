from setuptools import setup
setup(
    name='cli-anything-clear',
    version='1.0.0',
    packages=['cli_anything.clear'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-clear=cli_anything.clear:cli']},
)
