from setuptools import setup
setup(
    name='cli-anything-qdrant',
    version='1.0.0',
    packages=['cli_anything.qdrant'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-qdrant=cli_anything.qdrant:cli']},
)
