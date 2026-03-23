from setuptools import setup
setup(
    name='cli-anything-asset',
    version='1.0.0',
    packages=['cli_anything.asset'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-asset=cli_anything.asset:cli']},
)
