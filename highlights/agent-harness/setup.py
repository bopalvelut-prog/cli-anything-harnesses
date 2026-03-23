from setuptools import setup
setup(
    name='cli-anything-highlights',
    version='1.0.0',
    packages=['cli_anything.highlights'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-highlights=cli_anything.highlights:cli']},
)
