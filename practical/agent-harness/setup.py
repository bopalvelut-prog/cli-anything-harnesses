from setuptools import setup
setup(
    name='cli-anything-practical',
    version='1.0.0',
    packages=['cli_anything.practical'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-practical=cli_anything.practical:cli']},
)
