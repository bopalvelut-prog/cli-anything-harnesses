from setuptools import setup
setup(
    name='cli-anything-regolith',
    version='1.0.0',
    packages=['cli_anything.regolith'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-regolith=cli_anything.regolith:cli']},
)
