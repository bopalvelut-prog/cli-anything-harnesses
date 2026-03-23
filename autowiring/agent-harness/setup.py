from setuptools import setup
setup(
    name='cli-anything-autowiring',
    version='1.0.0',
    packages=['cli_anything.autowiring'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-autowiring=cli_anything.autowiring:cli']},
)
