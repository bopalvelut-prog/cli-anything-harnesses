from setuptools import setup
setup(
    name='cli-anything-kubeprobe',
    version='1.0.0',
    packages=['cli_anything.kubeprobe'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kubeprobe=cli_anything.kubeprobe:cli']},
)
