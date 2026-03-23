from setuptools import setup
setup(
    name='cli-anything-longhorn',
    version='1.0.0',
    packages=['cli_anything.longhorn'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-longhorn=cli_anything.longhorn:cli']},
)
