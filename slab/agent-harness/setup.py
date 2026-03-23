from setuptools import setup
setup(
    name='cli-anything-slab',
    version='1.0.0',
    packages=['cli_anything.slab'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-slab=cli_anything.slab:cli']},
)
