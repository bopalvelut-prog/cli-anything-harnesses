from setuptools import setup
setup(
    name='cli-anything-bone',
    version='1.0.0',
    packages=['cli_anything.bone'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bone=cli_anything.bone:cli']},
)
