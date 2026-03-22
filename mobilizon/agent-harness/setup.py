from setuptools import setup
setup(
    name='cli-anything-mobilizon',
    version='1.0.0',
    packages=['cli_anything.mobilizon'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mobilizon=cli_anything.mobilizon:cli']},
)
