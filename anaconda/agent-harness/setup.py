from setuptools import setup
setup(
    name='cli-anything-anaconda',
    version='1.0.0',
    packages=['cli_anything.anaconda'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-anaconda=cli_anything.anaconda:cli']},
)
