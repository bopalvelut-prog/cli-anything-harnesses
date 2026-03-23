from setuptools import setup
setup(
    name='cli-anything-park',
    version='1.0.0',
    packages=['cli_anything.park'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-park=cli_anything.park:cli']},
)
