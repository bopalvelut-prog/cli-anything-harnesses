from setuptools import setup
setup(
    name='cli-anything-mobile',
    version='1.0.0',
    packages=['cli_anything.mobile'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mobile=cli_anything.mobile:cli']},
)
