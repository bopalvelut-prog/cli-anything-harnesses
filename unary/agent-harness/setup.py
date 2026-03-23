from setuptools import setup
setup(
    name='cli-anything-unary',
    version='1.0.0',
    packages=['cli_anything.unary'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unary=cli_anything.unary:cli']},
)
