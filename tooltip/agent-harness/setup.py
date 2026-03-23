from setuptools import setup
setup(
    name='cli-anything-tooltip',
    version='1.0.0',
    packages=['cli_anything.tooltip'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tooltip=cli_anything.tooltip:cli']},
)
