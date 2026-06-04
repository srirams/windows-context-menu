# Custom context menu items for Windows

## What

Allows you to add custom items to the windows context menu. For example, an item called "resize" that displays on pictures to allow you to resize them.

## Why

There used to be a program called "FastExplorer" that allowed adding custom context menu items, but it no longer works with Windows 11 (random Explorer crashes)

You can add commands to the context menu using the registry ([docs](https://learn.microsoft.com/en-us/windows/win32/shell/context-menu-handlers#creating-static-cascading-menus)), but the drawback is that this method causes the command to be executed in parallel (eg if you select two files and execute your context menu item, explorer invokes your command twice, once for each item, instead of invoking the command once with the two files as arguments).

The only working solution is to use the Windows API COM interface.

## Alternatives

* https://defaultprogramseditor.com/ (untested)

* https://github.com/ikas-mc/ContextMenuForWindows11 (native windows 11 context menu items)

## How

[ExecuteCommand-Pipe](https://github.com/ge9/ExecuteCommand-Pipe), which implements the appropriate interfaces, is used to call a custom python script which then executes our custom command. I find that using a combination of editing the registry / python to be easier to maintain update and change.

## Setup

* Download and rename ExecuteCommand to ExecuteCommand400A.exe, and then run it.

* Update the windows registry so that ExecuteCommand will call our python script (make sure to correct the paths as appropriate for your system)
```Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Classes\CLSID\{FFA07888-75BD-471A-B325-59274E73400A}\LocalServer32]
@="D:\\Programs\\PyContext\\ExecuteCommand400A.exe a arg \"C:\\Windows\\pyw.exe\" \"D:\\Programs\\PyContext\\execute.py\" \"argv\" argf "
```

* Edit the `execute.py` to suit your needs.
* Edit the registry to add your custom item.
