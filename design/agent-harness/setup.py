from setuptools import setup
setup(
    name='cli-anything-design',
    version='1.0.0',
    packages=['cli_anything.design'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-design=cli_anything.design:cli']},
)
