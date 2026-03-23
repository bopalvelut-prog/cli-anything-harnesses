from setuptools import setup
setup(
    name='cli-anything-llamacpp',
    version='1.0.0',
    packages=['cli_anything.llamacpp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-llamacpp=cli_anything.llamacpp:cli']},
)
