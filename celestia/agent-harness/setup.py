from setuptools import setup
setup(
    name='cli-anything-celestia',
    version='1.0.0',
    packages=['cli_anything.celestia'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-celestia=cli_anything.celestia:cli']},
)
