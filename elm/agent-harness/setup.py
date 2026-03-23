from setuptools import setup
setup(
    name='cli-anything-elm',
    version='1.0.0',
    packages=['cli_anything.elm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-elm=cli_anything.elm:cli']},
)
