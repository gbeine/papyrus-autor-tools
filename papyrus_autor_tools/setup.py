from setuptools import setup

setup(name='papyrus_autor_tools',
      version='0.1',
      description='My toolchain for managing the Papyrus Autor references database',
      url='https://github.com/gbeine/papyrus-autor-tools',
      author='Gerrit Beine',
      author_email='mail@gerritbeine.de',
      license='MIT',
      packages=['papyrus_autor_tools'],
      requires=[
          'logging',
          'pyyaml',
        ],
      zip_safe=False)
