from setuptools import setup
setup(
    name='cli-anything-photos',
    version='1.0.0',
    packages=['cli_anything.photos'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-photos=cli_anything.photos:cli']},
)
