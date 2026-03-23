from setuptools import setup
setup(
    name='cli-anything-import',
    version='1.0.0',
    packages=['cli_anything.import'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-import=cli_anything.import:cli']},
)
