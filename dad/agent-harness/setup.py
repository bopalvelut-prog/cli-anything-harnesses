from setuptools import setup
setup(
    name='cli-anything-dad',
    version='1.0.0',
    packages=['cli_anything.dad'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dad=cli_anything.dad:cli']},
)
