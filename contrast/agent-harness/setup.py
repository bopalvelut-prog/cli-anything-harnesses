from setuptools import setup
setup(
    name='cli-anything-contrast',
    version='1.0.0',
    packages=['cli_anything.contrast'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-contrast=cli_anything.contrast:cli']},
)
