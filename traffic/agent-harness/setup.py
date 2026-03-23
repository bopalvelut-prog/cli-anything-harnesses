from setuptools import setup
setup(
    name='cli-anything-traffic',
    version='1.0.0',
    packages=['cli_anything.traffic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-traffic=cli_anything.traffic:cli']},
)
