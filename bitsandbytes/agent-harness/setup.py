from setuptools import setup
setup(
    name='cli-anything-bitsandbytes',
    version='1.0.0',
    packages=['cli_anything.bitsandbytes'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bitsandbytes=cli_anything.bitsandbytes:cli']},
)
