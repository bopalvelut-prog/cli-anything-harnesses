from setuptools import setup
setup(
    name='cli-anything-foundation',
    version='1.0.0',
    packages=['cli_anything.foundation'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-foundation=cli_anything.foundation:cli']},
)
