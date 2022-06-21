import cx_Freeze

executables = [cx_Freeze.Executable('alienG.py')]

cx_Freeze.setup(
    name="AlienG",
    options={'build_exe': {'packages':['pygame'],
                           'include_files':['assets']}},

    executables = executables
    
)