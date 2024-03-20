@echo off
echo.
echo   making Windows app...
echo.
pyinstaller --add-data "resource;resource" --name BDOLarkSearch -F -w -i icon.ico app.py

echo.
echo   making macOS app...
echo.
@REM pyinstaller --add-data resource:resource --name BDOLarkSearch -F -w -i icon.icns app.py

pause