from setuptools import setup
setup(
    name='cli-anything-slo',
    version='1.0.0',
    packages=['cli_anything.slo'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-slo=cli_anything.slo:cli']},
)
