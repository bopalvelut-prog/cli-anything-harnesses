from setuptools import setup
setup(
    name='cli-anything-darktable_cli',
    version='1.0.0',
    packages=['cli_anything.darktable_cli'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-darktable_cli=cli_anything.darktable_cli:cli']},
)
