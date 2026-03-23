from setuptools import setup
setup(
    name='cli-anything-asm',
    version='1.0.0',
    packages=['cli_anything.asm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-asm=cli_anything.asm:cli']},
)
