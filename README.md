# Hi!


This is an addon for SublimeLinter. It makes enabling/disabling registered linters better. 

First it adds a hook against Package Control. So, when you disable a package using Package Control it actually unregisters this linter immediately. No need to restart anymore. This kind of disabling is *persistent*.

Second, it adds a command to quickly enable/disable registered linters. Disabling a linter here is *global*, although the menu only shows linters that would work for the current view (to make the list shorter). This kind of disabling is only *in memory*.

The new command is called `sublime_linter_addon_toggle_linters` and it takes no arguments.

Bind it to a key e.g. 

```
  { "keys": ["ctrl+k", "ctrl+t"],
    "command": "sublime_linter_addon_toggle_linters"
  },
```

# Other

Adds a command to **toggle the debug mode** of SublimeLinter. Search for "SublimeLinter: Toggle debug mode" in the command palette. The internal name of that command is `sublime_linter_addon_toggle_debug`. 

# Install

Add this repo to `Package Control`.

1. Open up the command palette (`ctrl+shift+p`), and find `Package Control: Add Repository`. Then enter the URL of this repo: `https://github.com/kaste/SublimeLinter-addon-toggler` in the input field.
2. Open up the command palette again and find `Package Control: Install Package`, and just search for `SublimeLinter-addon-toggler`. (just a normal install)


