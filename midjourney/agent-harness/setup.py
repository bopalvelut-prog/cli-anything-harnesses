from setuptools import setup
setup(
    name='cli-anything-midjourney',
    version='1.0.0',
    packages=['cli_anything.midjourney'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-midjourney=cli_anything.midjourney:cli']},
)
