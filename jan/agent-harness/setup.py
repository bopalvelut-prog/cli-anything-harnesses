from setuptools import setup
setup(
    name='cli-anything-jan',
    version='1.0.0',
    packages=['cli_anything.jan'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jan=cli_anything.jan:cli']},
)
