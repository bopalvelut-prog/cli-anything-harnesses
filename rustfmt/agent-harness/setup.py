from setuptools import setup
setup(
    name='cli-anything-rustfmt',
    version='1.0.0',
    packages=['cli_anything.rustfmt'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rustfmt=cli_anything.rustfmt:cli']},
)
