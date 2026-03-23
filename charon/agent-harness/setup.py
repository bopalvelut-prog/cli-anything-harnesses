from setuptools import setup
setup(
    name='cli-anything-charon',
    version='1.0.0',
    packages=['cli_anything.charon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-charon=cli_anything.charon:cli']},
)
