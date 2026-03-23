from setuptools import setup
setup(
    name='cli-anything-real_10806',
    version='1.0.0',
    packages=['cli_anything.real_10806'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-real_10806=cli_anything.real_10806:cli']},
)
