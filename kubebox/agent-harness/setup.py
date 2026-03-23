from setuptools import setup
setup(
    name='cli-anything-kubebox',
    version='1.0.0',
    packages=['cli_anything.kubebox'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kubebox=cli_anything.kubebox:cli']},
)
