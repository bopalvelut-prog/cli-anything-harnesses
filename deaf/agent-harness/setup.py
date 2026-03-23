from setuptools import setup
setup(
    name='cli-anything-deaf',
    version='1.0.0',
    packages=['cli_anything.deaf'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-deaf=cli_anything.deaf:cli']},
)
