from setuptools import setup
setup(
    name='cli-anything-defrag',
    version='1.0.0',
    packages=['cli_anything.defrag'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-defrag=cli_anything.defrag:cli']},
)
