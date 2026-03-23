from setuptools import setup
setup(
    name='cli-anything-grief',
    version='1.0.0',
    packages=['cli_anything.grief'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-grief=cli_anything.grief:cli']},
)
