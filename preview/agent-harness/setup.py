from setuptools import setup
setup(
    name='cli-anything-preview',
    version='1.0.0',
    packages=['cli_anything.preview'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-preview=cli_anything.preview:cli']},
)
