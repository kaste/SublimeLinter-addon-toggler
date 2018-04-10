# Hi!


This is an addon for SublimeLinter. It adds a command to quickly enable/disable registered linters. Disabling a linter here is *global*, although the menu only shows linters that would work for the current view (to make the list shorter).

So the command is called `sublime_linter_addon_toggle_linters` and it takes no arguments.

Bind it to a key e.g. 

```
  { "keys": ["ctrl+k", "ctrl+t"],
    "command": "sublime_linter_addon_toggle_linters"
  },
```


# Install

Add this repo to `Package Control`.

1. Open up the command palette (`ctrl+shift+p`), and find `Package Control: Add Repository`. Then enter the URL of this repo: `https://github.com/kaste/SublimeLinter-addon-toggler` in the input field.
2. Open up the command palette again and find `Package Control: Install Package`, and just search for `SublimeLinter-addon-toggler`. (just a normal install)


