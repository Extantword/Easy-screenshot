if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit
python screen_cut.pyw

%SystemRoot%\explorer.exe %cd%
timeout /t 1
screenshot.png

exit