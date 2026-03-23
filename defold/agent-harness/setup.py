from setuptools import setup
setup(
    name='cli-anything-defold',
    version='1.0.0',
    packages=['cli_anything.defold'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-defold=cli_anything.defold:cli']},
)
