from setuptools import setup
setup(
    name='cli-anything-litestream',
    version='1.0.0',
    packages=['cli_anything.litestream'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-litestream=cli_anything.litestream:cli']},
)
