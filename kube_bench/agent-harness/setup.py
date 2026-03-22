from setuptools import setup
setup(
    name='cli-anything-kube_bench',
    version='1.0.0',
    packages=['cli_anything.kube_bench'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kube_bench=cli_anything.kube_bench:cli']},
)
