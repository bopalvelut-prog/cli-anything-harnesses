from setuptools import setup
setup(
    name='cli-anything-bake',
    version='1.0.0',
    packages=['cli_anything.bake'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bake=cli_anything.bake:cli']},
)
