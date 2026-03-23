from setuptools import setup
setup(
    name='cli-anything-break',
    version='1.0.0',
    packages=['cli_anything.break'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-break=cli_anything.break:cli']},
)
