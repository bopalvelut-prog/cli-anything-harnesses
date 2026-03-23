from setuptools import setup
setup(
    name='cli-anything-preload',
    version='1.0.0',
    packages=['cli_anything.preload'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-preload=cli_anything.preload:cli']},
)
