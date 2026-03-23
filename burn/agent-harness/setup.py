from setuptools import setup
setup(
    name='cli-anything-burn',
    version='1.0.0',
    packages=['cli_anything.burn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-burn=cli_anything.burn:cli']},
)
