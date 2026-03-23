from setuptools import setup
setup(
    name='cli-anything-ultimate',
    version='1.0.0',
    packages=['cli_anything.ultimate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ultimate=cli_anything.ultimate:cli']},
)
