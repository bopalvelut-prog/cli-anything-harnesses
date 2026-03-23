from setuptools import setup
setup(
    name='cli-anything-jcache',
    version='1.0.0',
    packages=['cli_anything.jcache'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jcache=cli_anything.jcache:cli']},
)
