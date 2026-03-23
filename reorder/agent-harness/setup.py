from setuptools import setup
setup(
    name='cli-anything-reorder',
    version='1.0.0',
    packages=['cli_anything.reorder'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-reorder=cli_anything.reorder:cli']},
)
