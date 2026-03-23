from setuptools import setup
setup(
    name='cli-anything-genuine',
    version='1.0.0',
    packages=['cli_anything.genuine'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-genuine=cli_anything.genuine:cli']},
)
