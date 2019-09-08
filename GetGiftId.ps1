$text = Get-Clipboard
return ($text | Select-String '^[A-Za-z0-9]{16}$') -Join ' '