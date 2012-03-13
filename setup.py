from setuptools import setup, find_packages

version = '0.1'

setup(name='malconstrict',
      version=version,
      description="Python wrapper to the Unofficial MyAnimeList API",
      long_description="Python wrapper to the Unofficial MyAnimeList API",
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2",
      ],
      keywords='myanimelist anime',
      author='Eitan Romanoff',
      author_email='ear7631@gmail.com',
      packages=find_packages(),
      url='http://github.com/ear7631/malconstrict',
      license='BSD',
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "requests",
      ],
      )