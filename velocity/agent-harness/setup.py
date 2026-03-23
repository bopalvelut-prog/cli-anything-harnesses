from setuptools import setup
setup(
    name='cli-anything-velocity',
    version='1.0.0',
    packages=['cli_anything.velocity'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-velocity=cli_anything.velocity:cli']},
)
