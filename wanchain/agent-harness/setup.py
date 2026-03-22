from setuptools import setup
setup(
    name='cli-anything-wanchain',
    version='1.0.0',
    packages=['cli_anything.wanchain'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wanchain=cli_anything.wanchain:cli']},
)
