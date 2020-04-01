proxycount = 15 ' Количество запускаемых прокси
countries = "" ' Например "{ru},{ua}". Пустое значение - любая страна
' НЕ РЕДАКТИРУЙТЕ ниже этой линии
' DO NOT EDIT below this line
Set FSO = CreateObject("Scripting.FileSystemObject") 
Set f = FSO.OpenTextFile("proxyList.txt", 2, True) 

For i=0 To proxycount-1 Step 1

	Port = 9000 + i
	CPort = 8000 + i
	
	If Not (countries = "") Then
            countries = " -ExitNodes " & countries
    End If
	
	Set WshShell = CreateObject("WScript.Shell")
	WshShell.Run "data\tor.exe -f data\torrc -SocksPort " & Port & " -ControlPort " & CPort & " -DataDirectory data\torf" & i & countries, 0
	WshShell = Null
	f.WriteLine "127.0.0.1:" & Port 


Next

f.Close 