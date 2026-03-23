from setuptools import setup
setup(
    name='cli-anything-media',
    version='1.0.0',
    packages=['cli_anything.media'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-media=cli_anything.media:cli']},
)
