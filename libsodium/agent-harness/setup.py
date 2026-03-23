from setuptools import setup
setup(
    name='cli-anything-libsodium',
    version='1.0.0',
    packages=['cli_anything.libsodium'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-libsodium=cli_anything.libsodium:cli']},
)
