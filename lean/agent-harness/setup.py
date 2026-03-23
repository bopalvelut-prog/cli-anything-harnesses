from setuptools import setup
setup(
    name='cli-anything-lean',
    version='1.0.0',
    packages=['cli_anything.lean'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lean=cli_anything.lean:cli']},
)
