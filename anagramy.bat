@echo off
:menu
cls
echo ==========================
echo           MENU
echo ==========================
echo 1. Uruchom anagramy
echo 2. Wyczysc historie programu
echo 3. Generuj raport
echo 4. Zamknij program
echo ==========================

set /p wybor="Wybierz opcje (wpisz numer): "

if "%wybor%"=="1" goto uruchom
if "%wybor%"=="2" goto wyczyscPlik
if "%wybor%"=="3" goto generujRaport
if "%wybor%"=="4" goto zamknijProgram

echo Bledny wybor. Wybierz ponownie.
timeout /nobreak /t 2 >nul
goto menu

:uruchom
echo Anagramy.
python "D:\projekty\j.skryptowe sem 3\anagramy.py"
pause
goto menu

:wyczyscPlik
echo Wyczyszczono plik.
type nul > "D:\projekty\j.skryptowe sem 3\raport.txt"
timeout /nobreak /t 2 >nul
goto menu

:generujRaport
@echo off
set "raport=D:\projekty\j.skryptowe sem 3\raport.html"

(
    echo ^<html^>
    echo    ^<head^>
    echo        ^<title^>Raport HTML^</title^>
    echo    ^</head^>
    echo    ^<body^>
    for /f "delims=" %%a in ('type "D:\projekty\j.skryptowe sem 3\raport.txt"') do echo        ^<p^>%%a^</p^>
    echo    ^</body^>
    echo ^</html^>
) > "%raport%"

echo Raport HTML zostal wygenerowany w pliku %raport%.
timeout /nobreak /t 2 >nul
goto menu

:zamknijProgram
timeout /nobreak /t 2 >nul
exit /b