from setuptools import setup
setup(
    name='cli-anything-distcc',
    version='1.0.0',
    packages=['cli_anything.distcc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-distcc=cli_anything.distcc:cli']},
)
