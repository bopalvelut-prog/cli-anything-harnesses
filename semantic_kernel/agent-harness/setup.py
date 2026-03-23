from setuptools import setup
setup(
    name='cli-anything-semantic_kernel',
    version='1.0.0',
    packages=['cli_anything.semantic_kernel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-semantic_kernel=cli_anything.semantic_kernel:cli']},
)
