from setuptools import setup
setup(
    name='cli-anything-worm',
    version='1.0.0',
    packages=['cli_anything.worm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-worm=cli_anything.worm:cli']},
)
