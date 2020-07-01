# -*- mode: python -*-

block_cipher = None


a = Analysis(['七段数码管绘制2.py'],
             pathex=['D:\\1\\作业题\\python'],
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
          name='七段数码管绘制2',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
