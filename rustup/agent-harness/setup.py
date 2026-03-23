from setuptools import setup
setup(
    name='cli-anything-rustup',
    version='1.0.0',
    packages=['cli_anything.rustup'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rustup=cli_anything.rustup:cli']},
)
