from setuptools import setup
setup(
    name='cli-anything-hero',
    version='1.0.0',
    packages=['cli_anything.hero'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-hero=cli_anything.hero:cli']},
)
