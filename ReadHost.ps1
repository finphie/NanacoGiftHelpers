using namespace System.Runtime.InteropServices

param([Parameter(Mandatory)]$text)
$message = Read-Host -Prompt $text -AsSecureString
$bstr = [Marshal]::SecureStringToBSTR($message)
$str = [Marshal]::PtrToStringBSTR($bstr)
[Marshal]::ZeroFreeBSTR($bstr)

return $str