@echo off

REM Check if "OneDrive\Escritorio" directory exists
if exist "%USERPROFILE%\OneDrive\Escritorio\" (
    set "LOCAL_FOLDER=OneDrive\Escritorio"
) else (
    set "LOCAL_FOLDER=Desktop"
)

REM Set the paths using the determined local folder
set "INSTALLER_PATH=%USERPROFILE%\%LOCAL_FOLDER%\local\python_installer.exe"
set "GIT_INSTALLER_PATH=%USERPROFILE%\%LOCAL_FOLDER%\local\git_installer.exe"

set "REPO_PATH=%USERPROFILE%\%LOCAL_FOLDER%\local\planBlocal"
set "CUSTOMIZE_LIB_PATH=%USERPROFILE%\%LOCAL_FOLDER%\local\customize_lib.py"


echo Checking if Python is already installed...
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Python is already installed.
) else (
    echo Python is not installed. Downloading the installer...
    bitsadmin /transfer "PythonInstaller" https://www.python.org/ftp/python/3.11.1/python-3.11.1-amd64.exe "%INSTALLER_PATH%"
    
    echo Installing Python...
    start /wait "" "%INSTALLER_PATH%" /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    echo Python installation complete.
)
pause
echo Instalando pip...
python -m ensurepip --default-pip
pause
echo Agregando pip al PATH...
setx /M PATH "%PATH%;%APPDATA%\Python\Python39\Scripts"
pause
echo Python y pip se han instalado correctamente.
echo Eliminando el instalador...
del "%INSTALLER_PATH%"
pause




echo Checking if Git is already installed...
git --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Git is already installed.
) else (
    echo Git is not installed. Downloading the installer...
    bitsadmin /transfer "GitInstaller" https://git-scm.com/download/win "%GIT_INSTALLER_PATH%"
    
    echo Installing Git...
    start /wait "" "%GIT_INSTALLER_PATH%" /SILENT
    echo Git installation complete.
)
pause



if not exist "%REPO_PATH%" (
    echo Cloning the repository...
    git clone https://github.com/ardu1na/local "%REPO_PATH%"
) else (
    echo The repository is already cloned.
)

cd "%REPO_PATH%"

pause
echo El repositorio planBlocal se ha clonado correctamente.
pause
echo Accediendo al repositorio...
cd "%REPO_PATH%"

echo Instalando librerías...
pip install -r requirements.txt

echo Las dependencias se han instalado correctamente.
pause



echo Modificando los archivos whats.py y core.py...
python "%CUSTOMIZE_LIB_PATH%"



pause
echo Casi listo...


python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations whatsapp
python manage.py migrate

pause
echo Aplicación configurada, puedes utilizar el archivo planb.bat para iniciar la aplicación
pause
echo Todo listo! Presiona cualquier tecla para salir.
pause
pause > nul
