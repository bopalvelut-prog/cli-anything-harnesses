from setuptools import setup
setup(
    name='cli-anything-real_10829',
    version='1.0.0',
    packages=['cli_anything.real_10829'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-real_10829=cli_anything.real_10829:cli']},
)
