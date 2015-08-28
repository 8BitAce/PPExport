# -*- mode: python -*-
#Gooey_languages and gooey_images are used to fetch the files and solve the problem that was occuring preivously. (i.e : Language file not found)
gooey_languages = Tree('C:/Python27/Lib/site-packages/gooey/languages', prefix = 'gooey/languages')
gooey_images = Tree('C:/Python27/Lib/site-packages/gooey/images', prefix = 'gooey/images')
a = Analysis(['ppexport.py'],
             pathex=['C:\\Users\\kscheiw1\\Desktop\\PPExport'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          gooey_languages,
          gooey_images,
          name='test.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )