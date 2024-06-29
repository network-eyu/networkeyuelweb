from distutils.core import setup
from pathlib import Path
# read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
  name = 'networkeyuelweb',
  packages = ['networkeyuelweb'],
  version = '1.0.1',
  license='MIT',
  description = 'Python package used to integrate networkeyuel web API',
  long_description= long_description,
  long_description_content_type= 'text/markdown',
  author = 'network-eyu',
  author_email = 'networkeyuel@duck.com',
  url = 'https://github.com/networkeyuel/networkeyuelweb',
  download_url = 'https://github.com/networkeyuel/networkeyuelweb/archive/refs/tags/v1.0.1.tar.gz', 
  install_requires=[
      'pycryptodome',
      'requests',
      'rsa',
      'six',
    ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',    
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
  ],
)
