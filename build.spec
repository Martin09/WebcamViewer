# -*- mode: python -*-
a = Analysis(['view_webcam.py'],
             pathex=[],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)

pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='MBECam',
          icon='dell.ico',
          debug=False,
          strip=False,
          upx=True,
          onefile=True,
          console=False)
