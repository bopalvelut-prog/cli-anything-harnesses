from setuptools import setup
setup(
    name='cli-anything-xargs',
    version='1.0.0',
    packages=['cli_anything.xargs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xargs=cli_anything.xargs:cli']},
)
