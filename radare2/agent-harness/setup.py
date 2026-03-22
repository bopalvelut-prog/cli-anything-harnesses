from setuptools import setup
setup(
    name='cli-anything-radare2',
    version='1.0.0',
    packages=['cli_anything.radare2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-radare2=cli_anything.radare2:cli']},
)
