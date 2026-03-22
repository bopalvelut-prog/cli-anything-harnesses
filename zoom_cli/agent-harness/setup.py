from setuptools import setup
setup(
    name='cli-anything-zoom_cli',
    version='1.0.0',
    packages=['cli_anything.zoom_cli'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zoom_cli=cli_anything.zoom_cli:cli']},
)
