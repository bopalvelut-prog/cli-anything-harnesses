from setuptools import setup
setup(
    name='cli-anything-aftereffects',
    version='1.0.0',
    packages=['cli_anything.aftereffects'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aftereffects=cli_anything.aftereffects:cli']},
)
