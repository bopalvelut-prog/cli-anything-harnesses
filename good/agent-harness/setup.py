from setuptools import setup
setup(
    name='cli-anything-good',
    version='1.0.0',
    packages=['cli_anything.good'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-good=cli_anything.good:cli']},
)
