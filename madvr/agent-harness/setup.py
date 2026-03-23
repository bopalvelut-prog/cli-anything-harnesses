from setuptools import setup
setup(
    name='cli-anything-madvr',
    version='1.0.0',
    packages=['cli_anything.madvr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-madvr=cli_anything.madvr:cli']},
)
