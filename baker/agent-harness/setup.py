from setuptools import setup
setup(
    name='cli-anything-baker',
    version='1.0.0',
    packages=['cli_anything.baker'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-baker=cli_anything.baker:cli']},
)
