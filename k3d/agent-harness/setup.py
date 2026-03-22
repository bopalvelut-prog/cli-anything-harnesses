from setuptools import setup
setup(
    name='cli-anything-k3d',
    version='1.0.0',
    packages=['cli_anything.k3d'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-k3d=cli_anything.k3d:cli']},
)
