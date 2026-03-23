from setuptools import setup
setup(
    name='cli-anything-tool',
    version='1.0.0',
    packages=['cli_anything.tool'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tool=cli_anything.tool:cli']},
)
