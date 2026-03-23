from setuptools import setup
setup(
    name='cli-anything-crazy',
    version='1.0.0',
    packages=['cli_anything.crazy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-crazy=cli_anything.crazy:cli']},
)
