from setuptools import setup
setup(
    name='cli-anything-numpy',
    version='1.0.0',
    packages=['cli_anything.numpy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-numpy=cli_anything.numpy:cli']},
)
