@echo off

echo Iniciando la aplicación planBlocal...

cd planBlocal


echo Presiona cualquier tecla para iniciar el servidor local y ejecutar la aplicación...
pause

start "Django Server" cmd /c "python manage.py runserver"

timeout /t 5 > nul

echo Esperando a que el servidor se inicie...


echo Abriendo Google Chrome en localhost:8000...
start "" /b /wait chrome --new-window http://localhost:8000


echo La aplicación se ha detenido. Presiona cualquier tecla para salir.
pause > nul
