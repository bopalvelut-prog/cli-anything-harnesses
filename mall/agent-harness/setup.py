from setuptools import setup
setup(
    name='cli-anything-mall',
    version='1.0.0',
    packages=['cli_anything.mall'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mall=cli_anything.mall:cli']},
)
