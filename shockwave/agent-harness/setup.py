from setuptools import setup
setup(
    name='cli-anything-shockwave',
    version='1.0.0',
    packages=['cli_anything.shockwave'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-shockwave=cli_anything.shockwave:cli']},
)
