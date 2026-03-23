from setuptools import setup
setup(
    name='cli-anything-enable',
    version='1.0.0',
    packages=['cli_anything.enable'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-enable=cli_anything.enable:cli']},
)
