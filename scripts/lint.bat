@echo off
setlocal
setlocal enabledelayedexpansion
pushd "%~dp0.."
set PYTHONUTF8=1
for /f "tokens=* usebackq" %%f in (`git ls-files "*.py"`) do ( set py_files=!py_files! %%f )
for /f "tokens=* usebackq" %%f in (`git ls-files "*.pyi"`) do ( set pyi_files=!pyi_files! %%f )
echo ### mypy ###
call poetry run mypy --show-error-codes %pyi_files%
echo ### flake8 ###
call poetry run flake8 --count --show-source --statistics %py_files% %pyi_files%
echo ### pyright ###
call poetry run pyright %py_files% %pyi_files%
echo ### pylint ###
call poetry run pylint %py_files% %pyi_files%
popd
endlocal
endlocal
pause
