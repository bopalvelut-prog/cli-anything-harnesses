from setuptools import setup
setup(
    name='cli-anything-webassembly',
    version='1.0.0',
    packages=['cli_anything.webassembly'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-webassembly=cli_anything.webassembly:cli']},
)
