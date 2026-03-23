from setuptools import setup
setup(
    name='cli-anything-arithmetic',
    version='1.0.0',
    packages=['cli_anything.arithmetic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-arithmetic=cli_anything.arithmetic:cli']},
)
