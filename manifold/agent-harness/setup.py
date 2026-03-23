from setuptools import setup
setup(
    name='cli-anything-manifold',
    version='1.0.0',
    packages=['cli_anything.manifold'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-manifold=cli_anything.manifold:cli']},
)
