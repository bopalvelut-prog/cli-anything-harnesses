from setuptools import setup
setup(
    name='cli-anything-dtach',
    version='1.0.0',
    packages=['cli_anything.dtach'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dtach=cli_anything.dtach:cli']},
)
