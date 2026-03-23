from setuptools import setup
setup(
    name='cli-anything-res',
    version='1.0.0',
    packages=['cli_anything.res'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-res=cli_anything.res:cli']},
)
