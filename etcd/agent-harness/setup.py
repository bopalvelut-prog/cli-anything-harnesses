from setuptools import setup
setup(
    name='cli-anything-etcd',
    version='1.0.0',
    packages=['cli_anything.etcd'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-etcd=cli_anything.etcd:cli']},
)
