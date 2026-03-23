from setuptools import setup
setup(
    name='cli-anything-gh',
    version='1.0.0',
    packages=['cli_anything.gh'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gh=cli_anything.gh:cli']},
)
