from setuptools import setup
setup(
    name='cli-anything-fence',
    version='1.0.0',
    packages=['cli_anything.fence'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-fence=cli_anything.fence:cli']},
)
