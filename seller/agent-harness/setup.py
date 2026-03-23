from setuptools import setup
setup(
    name='cli-anything-seller',
    version='1.0.0',
    packages=['cli_anything.seller'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-seller=cli_anything.seller:cli']},
)
