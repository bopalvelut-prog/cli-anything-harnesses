from setuptools import setup
setup(
    name='cli-anything-nasm',
    version='1.0.0',
    packages=['cli_anything.nasm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nasm=cli_anything.nasm:cli']},
)
