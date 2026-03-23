from setuptools import setup
setup(
    name='cli-anything-kubernetes_dashboard',
    version='1.0.0',
    packages=['cli_anything.kubernetes_dashboard'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kubernetes_dashboard=cli_anything.kubernetes_dashboard:cli']},
)
