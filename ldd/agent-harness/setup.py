from setuptools import setup
setup(
    name='cli-anything-ldd',
    version='1.0.0',
    packages=['cli_anything.ldd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ldd=cli_anything.ldd:cli']},
)
