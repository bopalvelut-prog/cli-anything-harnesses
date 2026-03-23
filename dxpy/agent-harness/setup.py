from setuptools import setup
setup(
    name='cli-anything-dxpy',
    version='1.0.0',
    packages=['cli_anything.dxpy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dxpy=cli_anything.dxpy:cli']},
)
