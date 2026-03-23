from setuptools import setup
setup(
    name='cli-anything-force',
    version='1.0.0',
    packages=['cli_anything.force'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-force=cli_anything.force:cli']},
)
