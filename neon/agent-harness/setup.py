from setuptools import setup
setup(
    name='cli-anything-neon',
    version='1.0.0',
    packages=['cli_anything.neon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-neon=cli_anything.neon:cli']},
)
