from setuptools import setup
setup(
    name='cli-anything-buildkit',
    version='1.0.0',
    packages=['cli_anything.buildkit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-buildkit=cli_anything.buildkit:cli']},
)
