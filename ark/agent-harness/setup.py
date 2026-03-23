from setuptools import setup
setup(
    name='cli-anything-ark',
    version='1.0.0',
    packages=['cli_anything.ark'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ark=cli_anything.ark:cli']},
)
