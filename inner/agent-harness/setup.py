from setuptools import setup
setup(
    name='cli-anything-inner',
    version='1.0.0',
    packages=['cli_anything.inner'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-inner=cli_anything.inner:cli']},
)
