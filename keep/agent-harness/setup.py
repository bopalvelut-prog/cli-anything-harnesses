from setuptools import setup
setup(
    name='cli-anything-keep',
    version='1.0.0',
    packages=['cli_anything.keep'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-keep=cli_anything.keep:cli']},
)
