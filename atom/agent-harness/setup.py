from setuptools import setup
setup(
    name='cli-anything-atom',
    version='1.0.0',
    packages=['cli_anything.atom'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-atom=cli_anything.atom:cli']},
)
