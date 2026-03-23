from setuptools import setup
setup(
    name='cli-anything-protein',
    version='1.0.0',
    packages=['cli_anything.protein'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-protein=cli_anything.protein:cli']},
)
