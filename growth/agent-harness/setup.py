from setuptools import setup
setup(
    name='cli-anything-growth',
    version='1.0.0',
    packages=['cli_anything.growth'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-growth=cli_anything.growth:cli']},
)
