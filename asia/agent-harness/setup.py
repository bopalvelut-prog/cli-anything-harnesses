from setuptools import setup
setup(
    name='cli-anything-asia',
    version='1.0.0',
    packages=['cli_anything.asia'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-asia=cli_anything.asia:cli']},
)
