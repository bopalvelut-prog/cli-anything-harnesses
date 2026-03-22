from setuptools import setup
setup(
    name='cli-anything-trezor',
    version='1.0.0',
    packages=['cli_anything.trezor'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-trezor=cli_anything.trezor:cli']},
)
