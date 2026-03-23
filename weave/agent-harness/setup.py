from setuptools import setup
setup(
    name='cli-anything-weave',
    version='1.0.0',
    packages=['cli_anything.weave'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-weave=cli_anything.weave:cli']},
)
