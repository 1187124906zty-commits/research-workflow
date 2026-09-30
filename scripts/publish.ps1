param(
    [string]$RepositoryName = 'research-workflow',
    [ValidateSet('public','private')][string]$Visibility = 'public'
)
$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$ghCommand = Get-Command gh -ErrorAction SilentlyContinue
if ($ghCommand) { $ghPath = $ghCommand.Source }
else {
    $ghPath = Join-Path $env:LOCALAPPDATA 'researchflow-tools/gh/bin/gh.exe'
    if (-not (Test-Path -LiteralPath $ghPath)) { throw 'Install GitHub CLI from cli.github.com before publishing.' }
}
Push-Location -LiteralPath $repoRoot
try {
    & $ghPath auth status
    if ($LASTEXITCODE -ne 0) { throw 'GitHub login is required. Run gh auth login --web, then rerun this script.' }
    $dirty = & git status --porcelain
    if ($LASTEXITCODE -ne 0) { throw 'This directory must be a Git repository.' }
    if ($dirty) { throw 'Commit the reviewed release files before publishing.' }
    $origin = & git remote get-url origin 2>$null
    if ($LASTEXITCODE -eq 0 -and $origin) {
        & git push -u origin HEAD
        if ($LASTEXITCODE -ne 0) { throw 'Push failed; preserve the local commit and resolve the reported error.' }
    } else {
        & $ghPath repo create $RepositoryName "--$Visibility" --source . --remote origin --push `
          --description 'Evidence-bound multi-agent research workflows for Codex, PaperSpine and simulation projects'
        if ($LASTEXITCODE -ne 0) { throw 'Repository creation or initial push failed; inspect the returned state before retrying.' }
    }
    & $ghPath repo view --json url,nameWithOwner
    if ($LASTEXITCODE -ne 0) { throw 'Could not verify the published repository.' }
} finally {
    Pop-Location
}
