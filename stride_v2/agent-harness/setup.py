from setuptools import setup
setup(
    name='cli-anything-stride_v2',
    version='1.0.0',
    packages=['cli_anything.stride_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stride_v2=cli_anything.stride_v2:cli']},
)
