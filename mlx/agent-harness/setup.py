from setuptools import setup
setup(
    name='cli-anything-mlx',
    version='1.0.0',
    packages=['cli_anything.mlx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mlx=cli_anything.mlx:cli']},
)
