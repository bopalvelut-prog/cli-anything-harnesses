from setuptools import setup
setup(
    name='cli-anything-arnold',
    version='1.0.0',
    packages=['cli_anything.arnold'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-arnold=cli_anything.arnold:cli']},
)
