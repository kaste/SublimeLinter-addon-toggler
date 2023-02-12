# Hi!


This is an addon for SublimeLinter. 

## Enabling/disabling registered linters 

First it adds a hook against Package Control. So, when you disable a package using Package Control
it actually unregisters this linter immediately. No need to restart anymore. This kind of disabling
is *persistent*.

Second, it adds a command to quickly enable/disable registered linters. The new command is called
`sublime_linter_addon_toggle_linters` and it may optionally take an argument.

Bind it to a key e.g.

```
  { "keys": ["ctrl+k", "ctrl+t"],
    "command": "sublime_linter_addon_toggle_linters"
    "args": {"persist": "project"}  // optional
  },
```

If you don't set "persist" then disabling a linter is *global* for all open windows, but also
only *in memory*.  Currently only "project" is implemented and saves the configuration in the open
project file.

## Toggle debug mode

Adds a command to **toggle the debug mode** of SublimeLinter. Search for "SublimeLinter: Toggle
debug mode" in the command palette. The internal name of that command is
`sublime_linter_addon_toggle_debug`.

## Switch lint mode

Adds a command to quickly **switch the lint mode** of SublimeLinter. Search for "SublimeLinter:
Switch lint mode". The command is called `sublime_linter_addon_choose_lint_mode` and it takes
`lint_mode` as an *optional* argument.

# Install

Add this repo to `Package Control`.

1. Open up the command palette (`ctrl+shift+p`), and find `Package Control: Add Repository`. Then
enter the URL of this repo: `https://github.com/kaste/SublimeLinter-addon-toggler` in the input
field.

2. Open up the command palette again and find `Package Control: Install Package`, and just
search for `SublimeLinter-addon-toggler`. (just a normal install)


