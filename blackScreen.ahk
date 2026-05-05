myGui1 := 0
myGui2 := 0
screenColor := "Black"

; === PrintScreen: Toggle (encender/apagar ambas pantallas) ===
PrintScreen:: {
    global myGui1, myGui2, screenColor

    ; Si ya están activas → apagar
    if (myGui1 || myGui2) {
        if myGui1 {
            myGui1.Destroy()
            myGui1 := 0
        }
        if myGui2 {
            myGui2.Destroy()
            myGui2 := 0
        }
        return
    }

    ; Si están apagadas → encender
    ; Pantalla principal
    myGui1 := Gui("+AlwaysOnTop -Caption +ToolWindow")
    myGui1.BackColor := screenColor
    myGui1.Show("x0 y0 w" A_ScreenWidth " h" A_ScreenHeight)

    ; Segunda pantalla (si existe)
    if MonitorGetCount() >= 2 {
        MonitorGet(2, &left, &top, &right, &bottom)
        width := right - left
        height := bottom - top

        myGui2 := Gui("+AlwaysOnTop -Caption +ToolWindow")
        myGui2.BackColor := screenColor
        myGui2.Show("x" left " y" top " w" width " h" height)
    }
}