from setuptools import setup
setup(
    name='cli-anything-revenue',
    version='1.0.0',
    packages=['cli_anything.revenue'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-revenue=cli_anything.revenue:cli']},
)
