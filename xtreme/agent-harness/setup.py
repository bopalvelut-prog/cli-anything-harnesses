from setuptools import setup
setup(
    name='cli-anything-xtreme',
    version='1.0.0',
    packages=['cli_anything.xtreme'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xtreme=cli_anything.xtreme:cli']},
)
