from setuptools import setup
setup(
    name='cli-anything-uv_python',
    version='1.0.0',
    packages=['cli_anything.uv_python'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-uv_python=cli_anything.uv_python:cli']},
)
