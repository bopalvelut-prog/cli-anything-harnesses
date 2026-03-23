from setuptools import setup
setup(
    name='cli-anything-xxhash',
    version='1.0.0',
    packages=['cli_anything.xxhash'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-xxhash=cli_anything.xxhash:cli']},
)
