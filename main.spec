# -*- mode: python -*-
'''usage: python3 path/to/pyinstaller.py main.spec'''

block_cipher = None

a = Analysis(['./main.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=False )

app = BUNDLE(exe,
             name='Coda.app',
             icon='./resources/icon/coda.icns',
             bundle_identifier=None,
             version='0.0.3',
             info_plist={
                'NSHighResolutionCapable': 'True'
             }
         )
