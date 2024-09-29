from setuptools import Extension
from setuptools.dist import Distribution
from setuptools.command.build_ext import build_ext

def build(setup_kwargs):
    base64c_module = Extension(
        'base64c',
        sources=['src/base64c.c'],
        extra_compile_args=['-O3', '-march=native']
    )
    
    class BuildExt(build_ext):
        def run(self):
            build_ext.run(self)

        def build_extension(self, ext):
            build_ext.build_extension(self, ext)

    dist = Distribution({'name': 'base64c', 'ext_modules': [base64c_module]})
    cmd = BuildExt(dist)
    cmd.ensure_finalized()
    cmd.run()

    setup_kwargs.update({
        'ext_modules': [base64c_module],
        'cmdclass': {'build_ext': BuildExt},
        'package_data': {'base64c': ['base64c.pyi']},
    })