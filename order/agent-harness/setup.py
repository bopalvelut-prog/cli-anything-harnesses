from setuptools import setup
setup(
    name='cli-anything-order',
    version='1.0.0',
    packages=['cli_anything.order'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-order=cli_anything.order:cli']},
)
