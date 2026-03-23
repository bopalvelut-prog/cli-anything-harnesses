from setuptools import setup
setup(
    name='cli-anything-clerk',
    version='1.0.0',
    packages=['cli_anything.clerk'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-clerk=cli_anything.clerk:cli']},
)
