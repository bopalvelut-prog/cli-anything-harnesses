from setuptools import setup
setup(
    name='cli-anything-san',
    version='1.0.0',
    packages=['cli_anything.san'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-san=cli_anything.san:cli']},
)
