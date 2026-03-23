from setuptools import setup
setup(
    name='cli-anything-index',
    version='1.0.0',
    packages=['cli_anything.index'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-index=cli_anything.index:cli']},
)
