from setuptools import setup
setup(
    name='cli-anything-wheel',
    version='1.0.0',
    packages=['cli_anything.wheel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wheel=cli_anything.wheel:cli']},
)
