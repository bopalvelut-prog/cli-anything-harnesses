from setuptools import setup
setup(
    name='cli-anything-linode_storage',
    version='1.0.0',
    packages=['cli_anything.linode_storage'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-linode_storage=cli_anything.linode_storage:cli']},
)
