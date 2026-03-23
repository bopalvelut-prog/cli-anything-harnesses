from setuptools import setup
setup(
    name='cli-anything-dataproc',
    version='1.0.0',
    packages=['cli_anything.dataproc'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dataproc=cli_anything.dataproc:cli']},
)
