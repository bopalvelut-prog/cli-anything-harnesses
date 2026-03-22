from setuptools import setup
setup(
    name='cli-anything-kube_hunter',
    version='1.0.0',
    packages=['cli_anything.kube_hunter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kube_hunter=cli_anything.kube_hunter:cli']},
)
