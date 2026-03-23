from setuptools import setup
setup(
    name='cli-anything-real_10853',
    version='1.0.0',
    packages=['cli_anything.real_10853'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-real_10853=cli_anything.real_10853:cli']},
)
