from setuptools import setup
setup(
    name='cli-anything-detail',
    version='1.0.0',
    packages=['cli_anything.detail'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-detail=cli_anything.detail:cli']},
)
