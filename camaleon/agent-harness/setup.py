from setuptools import setup
setup(
    name='cli-anything-camaleon',
    version='1.0.0',
    packages=['cli_anything.camaleon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-camaleon=cli_anything.camaleon:cli']},
)
