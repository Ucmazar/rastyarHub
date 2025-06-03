@echo off
echo 🔄 Pulling latest changes...
git pull origin main

echo.
echo ➕ Adding all changes...
git add .

set /p message=📝 Enter commit message: 

git commit -m "%message%"

echo.
echo 🚀 Pushing to GitHub...
git push origin main

echo.
echo ✅ Done!
<<<<<<< HEAD
pause
=======
pause
>>>>>>> 69cd72425ac558c2457731fb9c3e7e2128128d8b