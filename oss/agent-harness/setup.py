from setuptools import setup
setup(
    name='cli-anything-oss',
    version='1.0.0',
    packages=['cli_anything.oss'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-oss=cli_anything.oss:cli']},
)
