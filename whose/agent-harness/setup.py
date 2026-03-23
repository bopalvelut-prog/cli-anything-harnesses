from setuptools import setup
setup(
    name='cli-anything-whose',
    version='1.0.0',
    packages=['cli_anything.whose'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-whose=cli_anything.whose:cli']},
)
