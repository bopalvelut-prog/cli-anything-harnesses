from setuptools import setup
setup(
    name='cli-anything-decrease',
    version='1.0.0',
    packages=['cli_anything.decrease'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-decrease=cli_anything.decrease:cli']},
)
