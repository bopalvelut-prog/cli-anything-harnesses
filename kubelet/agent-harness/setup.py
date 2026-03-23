from setuptools import setup
setup(
    name='cli-anything-kubelet',
    version='1.0.0',
    packages=['cli_anything.kubelet'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kubelet=cli_anything.kubelet:cli']},
)
