import cx_Freeze
executables=[
    cx_Freeze.Executable(script='main.py',icon='space.ico')
]
cx_Freeze.setup(
    name='Space Marker',
    options={
        'build_exe':{
            'packages':['pygame'],
            'include_files':[
                'bg.jpg',
                'space.png'
                'soundtrack.mp3'
            ]
        }
    }, executables=executables
)

#python geraSetup.py build
#python geraSetup.py bdist_msi