from setuptools import setup
setup(
    name='cli-anything-kobold',
    version='1.0.0',
    packages=['cli_anything.kobold'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kobold=cli_anything.kobold:cli']},
)
