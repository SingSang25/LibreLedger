param (
    [string]$Path = ".",
    [int]$Depth = 4,
    [string[]]$IgnoreFolders = @(".venv", "node_modules", "__pycache__", ".git")
)

function Get-Tree($folder, $prefix = "", $level = 1, $maxDepth = 10, $ignore = @()) {
    if ($level -gt $maxDepth) {
        return
    }

    $items = Get-ChildItem -Path $folder -Force | Where-Object {
        $_.PSIsContainer -and ($ignore -notcontains $_.Name) -or -not $_.PSIsContainer
    } | Sort-Object { if ($_.PSIsContainer) { "0$($_.Name)" } else { "1$($_.Name)" } }

    $count = $items.Count
    for ($i = 0; $i -lt $count; $i++) {
        $item = $items[$i]
        $isLast = ($i -eq $count - 1)
        $connector = if ($isLast) { "└── " } else { "├── " }
        Write-Output "$prefix$connector$item.Name"

        if ($item.PSIsContainer -and ($ignore -notcontains $item.Name)) {
            $newPrefix = if ($isLast) { "$prefix    " } else { "$prefix│   " }
            Get-Tree -folder $item.FullName -prefix $newPrefix -level ($level + 1) -maxDepth $maxDepth -ignore $ignore
        }
    }
}

# Start
Write-Output "`n📁 Projektstruktur mit Dateien (max. Tiefe: $Depth, ohne: $IgnoreFolders):"
Get-Tree -folder (Resolve-Path $Path) -maxDepth $Depth -ignore $IgnoreFolders
