from setuptools import setup
setup(
    name='cli-anything-kube_state',
    version='1.0.0',
    packages=['cli_anything.kube_state'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kube_state=cli_anything.kube_state:cli']},
)
