param(
    [Parameter(Mandatory = $true, HelpMessage = "Folder to visualize as a tree")]
    [ValidateNotNullOrEmpty()]
    [string]$Path,

    # If set, directory names won't be printed (only files are shown as leaves)
    [switch]$FilesOnly,

    # Optional depth limit (default: unlimited)
    [int]$MaxDepth = [int]::MaxValue,

    # If set, include hidden items (otherwise they are ignored)
    [switch]$IncludeHidden
)

function Show-Tree {
    param(
        [string]$CurrentPath,
        [string]$Prefix = "",
        [int]$Depth = 0
    )

    if ($Depth -ge $MaxDepth) { return }

    try {
        # Build common parameters and only pass -Force when IncludeHidden is set
        $commonParams = @{
            LiteralPath = $CurrentPath
            ErrorAction = 'Stop'
            Force       = $IncludeHidden
        }

        # Separate directories and files to list folders first
        $dirs = Get-ChildItem @commonParams -Directory | Sort-Object Name
        $files = Get-ChildItem @commonParams -File      | Sort-Object Name

        # We iterate dirs first, then files
        $items = @()
        $items += $dirs
        $items += $files
    }
    catch {
        Write-Warning "$Prefix└── <access denied>: $CurrentPath"
        return
    }

    for ($i = 0; $i -lt $items.Count; $i++) {
        $item = $items[$i]

        # Always ignore "__pycache__" directories
        if ($item.PSIsContainer -and ($item.Name -ieq '__pycache__')) { continue }
        if ($item.PSIsContainer -and ($item.Name -ieq '.pytest_cache')) { continue }
        if ($item.PSIsContainer -and ($item.Name -ieq '.sonarlint')) { continue }
        if ($item.PSIsContainer -and ($item.Name -ieq '.vscode')) { continue }
        if ($item.PSIsContainer -and ($item.Name -ieq '.venv')) { continue }

        $isLast = ($i -eq $items.Count - 1)
        $joint = if ($isLast) { "└── " } else { "├── " }
        $pad = if ($isLast) { "    " } else { "│   " }

        if ($item.PSIsContainer) {
            if (-not $FilesOnly) {
                Write-Host ($Prefix + $joint + $item.Name)
            }
            # Recurse into subdirectory
            Show-Tree -CurrentPath $item.FullName -Prefix ($Prefix + $pad) -Depth ($Depth + 1)
        }
        else {
            Write-Host ($Prefix + $joint + $item.Name)
        }
    }
}

# Normalize and print root
try {
    $root = (Resolve-Path -LiteralPath $Path -ErrorAction Stop).Path
}
catch {
    throw "Path not found: $Path"
}

if (-not $FilesOnly) {
    Write-Host $root
}
Show-Tree -CurrentPath $root