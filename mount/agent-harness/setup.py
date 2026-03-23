from setuptools import setup
setup(
    name='cli-anything-mount',
    version='1.0.0',
    packages=['cli_anything.mount'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mount=cli_anything.mount:cli']},
)
