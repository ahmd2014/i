from fleet import *
def main(page:Page):
   
        page.title = "flash app"
        page.scroll = "auto"
        page.window.width = 390
        page.window.height = 740
        page.window.top = 1
        page.window.left = 960
        page.bgcolor = 'white'
        page.theme_mode = ThemeMode.LIGHT
        flashlight = Flashlight()
        page.overlay.append(flashlight)
        ph = PermissionHandler()
        page.overlay.append(ph)
        def o(e):     
            ph.open_app_settings()


        page.add(

    AppBar(
        title=Text('Flash light app'),
        color='black',
        bgcolor='#9aede0',
        actions=[
            IconButton(icons.SETTINGS,on_click=lambda _: o)
        ]
    ),
    Row([
        Text('\n\nFlash light',size=31,color='black')
         ],alignment=MainAxisAlignment.CENTER),
         Row([
           Image(src="y.jpg",width=200)  
         ],alignment=MainAxisAlignment.CENTER),
         Row([
             ElevatedButton(
                 "ON",
                 width=100,
                 icon=icons.PLAY_ARROW,
                 style=ButtonStyle(
                 bgcolor="#9aede0",
                 color='white',
                 padding=15,
                 shape=ContinuousRectangleBorder(radius=100),
                         ),
                    on_click=lambda _: flashlight.turn_on()                
                    ),
                 ElevatedButton(
                 "OFF",
                 width=100,
                 icon=icons.PLAY_DISABLED_SHARP,
                 style=ButtonStyle(
                 bgcolor="#9aede0",
                 color='white',
                 padding=15,
                 shape=ContinuousRectangleBorder(radius=100)
                 ),
                 on_click=lambda _: flashlight.turn_off()
                 ),
         ],alignment=MainAxisAlignment.CENTER),
              
    )
        page.update()
app(main)