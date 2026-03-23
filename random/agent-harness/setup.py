from setuptools import setup
setup(
    name='cli-anything-random',
    version='1.0.0',
    packages=['cli_anything.random'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-random=cli_anything.random:cli']},
)
