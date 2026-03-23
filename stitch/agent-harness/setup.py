from setuptools import setup
setup(
    name='cli-anything-stitch',
    version='1.0.0',
    packages=['cli_anything.stitch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stitch=cli_anything.stitch:cli']},
)
