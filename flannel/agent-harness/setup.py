from setuptools import setup
setup(
    name='cli-anything-flannel',
    version='1.0.0',
    packages=['cli_anything.flannel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-flannel=cli_anything.flannel:cli']},
)
