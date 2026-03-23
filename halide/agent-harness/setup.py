from setuptools import setup
setup(
    name='cli-anything-halide',
    version='1.0.0',
    packages=['cli_anything.halide'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-halide=cli_anything.halide:cli']},
)
