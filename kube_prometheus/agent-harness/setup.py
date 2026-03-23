from setuptools import setup
setup(
    name='cli-anything-kube_prometheus',
    version='1.0.0',
    packages=['cli_anything.kube_prometheus'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kube_prometheus=cli_anything.kube_prometheus:cli']},
)
