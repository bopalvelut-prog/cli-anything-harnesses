from setuptools import setup
setup(
    name='cli-anything-nearly',
    version='1.0.0',
    packages=['cli_anything.nearly'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-nearly=cli_anything.nearly:cli']},
)
