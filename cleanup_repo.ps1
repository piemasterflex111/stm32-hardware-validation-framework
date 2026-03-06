# =========================
# Repo cleanup script
# =========================

Write-Host "Starting repo cleanup..."

# 1. Ensure we are in repo
git rev-parse --is-inside-work-tree 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "Not inside a git repo."
    exit
}

# 2. Create professional repo structure
New-Item -ItemType Directory -Force -Path docs | Out-Null
New-Item -ItemType Directory -Force -Path tests | Out-Null
New-Item -ItemType Directory -Force -Path src | Out-Null

# 3. Remove junk files from git index
git rm -r --cached .venv 2>$null
git rm -r --cached results 2>$null
git rm -r --cached __pycache__ 2>$null
git rm -r --cached docs/_private 2>$null
git rm -r --cached *.log 2>$null

# 4. Rebuild .gitignore cleanly
@"
# Python
__pycache__/
*.pyc
.venv/

# Editor
.vscode/

# Test artifacts
results/
artifacts/

# Private notes
docs/_private/

# OS junk
Thumbs.db
Desktop.ini
"@ | Set-Content .gitignore

# 5. Stage everything clean
git add .

# 6. Commit cleanup
git commit -m "repo cleanup: normalize structure, enforce gitignore"

# 7. Push
git push origin main

Write-Host "Cleanup complete."