from setuptools import setup
setup(
    name='cli-anything-edge',
    version='1.0.0',
    packages=['cli_anything.edge'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-edge=cli_anything.edge:cli']},
)
