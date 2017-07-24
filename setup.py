from setuptools import setup

setup(name='pydpyp',
      version='0.1',
      description='Manage playlists from both Spotify and Google Play Music',
      url='https://github.com/bobbywlindsey/pydpyp',
      author='Bobby Lindsey',
      author_email='me@bobbywlindsey.com',
      license='MIT',
      packages=['pydpyp'],
      install_requires=[
          'spotipy',
          'gmusicapi',
      ],
      )
