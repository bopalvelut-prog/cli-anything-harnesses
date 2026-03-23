from setuptools import setup
setup(
    name='cli-anything-full',
    version='1.0.0',
    packages=['cli_anything.full'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-full=cli_anything.full:cli']},
)
