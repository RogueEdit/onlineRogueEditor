# -*- mode: python ; coding: utf-8 -*-

added_files = [
    ('../../src/utilities/*.py', 'utilities'),
    ('../../src/modules/*.py', 'modules')
]


a = Analysis(
    ['../../src/main.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=['_cffi_backend'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='pyRogue-MacIntel.sh',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
