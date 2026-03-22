from setuptools import setup
setup(
    name='cli-anything-bazarr',
    version='1.0.0',
    packages=['cli_anything.bazarr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bazarr=cli_anything.bazarr:cli']},
)
