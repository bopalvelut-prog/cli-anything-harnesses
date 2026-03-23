from setuptools import setup
setup(
    name='cli-anything-kpatch',
    version='1.0.0',
    packages=['cli_anything.kpatch'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kpatch=cli_anything.kpatch:cli']},
)
