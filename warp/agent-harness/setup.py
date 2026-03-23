from setuptools import setup
setup(
    name='cli-anything-warp',
    version='1.0.0',
    packages=['cli_anything.warp'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-warp=cli_anything.warp:cli']},
)
