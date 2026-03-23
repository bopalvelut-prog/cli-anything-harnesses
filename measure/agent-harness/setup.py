from setuptools import setup
setup(
    name='cli-anything-measure',
    version='1.0.0',
    packages=['cli_anything.measure'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-measure=cli_anything.measure:cli']},
)
