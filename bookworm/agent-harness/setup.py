from setuptools import setup
setup(
    name='cli-anything-bookworm',
    version='1.0.0',
    packages=['cli_anything.bookworm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bookworm=cli_anything.bookworm:cli']},
)
