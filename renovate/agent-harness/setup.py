from setuptools import setup
setup(
    name='cli-anything-renovate',
    version='1.0.0',
    packages=['cli_anything.renovate'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-renovate=cli_anything.renovate:cli']},
)
