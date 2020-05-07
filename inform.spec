# -*- mode: python -*-

block_cipher = None


a = Analysis(['inform.py'],
             pathex=['D:\\迅雷下载\\小蜜蜂开发环境搭建\\pywinauto_env_build\\快期自动化操作_源码'],
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
          name='inform',
          debug=False,
          strip=False,
          upx=True,
          console=True )
