from setuptools import setup
setup(
    name='cli-anything-obs',
    version='1.0.0',
    packages=['cli_anything.obs'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-obs=cli_anything.obs:cli']},
)
