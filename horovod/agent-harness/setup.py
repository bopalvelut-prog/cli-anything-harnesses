from setuptools import setup
setup(
    name='cli-anything-horovod',
    version='1.0.0',
    packages=['cli_anything.horovod'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-horovod=cli_anything.horovod:cli']},
)
