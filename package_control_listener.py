import sublime
from SublimeLinter.lint import persist

USER_PREFERENCES_FILE = 'Preferences.sublime-settings'
PACKAGE_CONTROL_PREFERENCES_FILE = 'Package Control.sublime-settings'
PREFERENCES_OBSERVER_KEY = 'SL-addon-toggler'

USER_SETTINGS = None
PACKAGE_CONTROL_SETTINGS = None

State = {'disabled': set()}


def plugin_loaded():
    global USER_SETTINGS, PACKAGE_CONTROL_SETTINGS

    USER_SETTINGS = sublime.load_settings(USER_PREFERENCES_FILE)
    PACKAGE_CONTROL_SETTINGS = sublime.load_settings(
        PACKAGE_CONTROL_PREFERENCES_FILE
    )

    USER_SETTINGS.add_on_change(PREFERENCES_OBSERVER_KEY, on_change)
    PACKAGE_CONTROL_SETTINGS.add_on_change(PREFERENCES_OBSERVER_KEY, on_change)

    State.update({'disabled': disabled_plugins()})


def plugin_unloaded():
    USER_SETTINGS.clear_on_change(PREFERENCES_OBSERVER_KEY)
    PACKAGE_CONTROL_SETTINGS.clear_on_change(PREFERENCES_OBSERVER_KEY)


def on_change():
    # Using defer to 'combine' or merge changes that occur on user and package
    # control settings at nearly the same time.
    sublime.set_timeout_async(_on_change, 100)


def _on_change():
    current_state = State.get('disabled')
    next_state = disabled_plugins()

    newly_disabled_plugins = next_state - current_state
    if newly_disabled_plugins:
        affected_linters = {
            name
            for name, klass in persist.linter_classes.items()
            if klass.__module__.split('.')[0] in newly_disabled_plugins
        }

        if affected_linters:
            for name in affected_linters:
                persist.linter_classes.pop(name)

            sublime.run_command('sublime_linter_config_changed')

    State.update({'disabled': next_state})


def disabled_plugins():
    ignored = set(USER_SETTINGS.get('ignored_packages', []))
    in_situ = set(PACKAGE_CONTROL_SETTINGS.get('in_process_packages', []))

    really_ignored = ignored - in_situ
    return really_ignored
