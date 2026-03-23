from setuptools import setup
setup(
    name='cli-anything-wm',
    version='1.0.0',
    packages=['cli_anything.wm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wm=cli_anything.wm:cli']},
)
