from setuptools import setup
setup(
    name='cli-anything-gauge',
    version='1.0.0',
    packages=['cli_anything.gauge'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gauge=cli_anything.gauge:cli']},
)
