import sublime
import sublime_plugin

from SublimeLinter.lint import persist, linter


LAST_TOGGLED_LINTER_CLASS = None


class sublime_linter_addon_toggle_linters(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        linters = collect_possible_linters(view)
        if not linters:
            self.window.status_message(
                'No possible linters registered for this view. :-(')
            return

        items = [text for _, _, text in linters]
        try:
            selected = next(
                i for i, (_, linter_class, _) in enumerate(linters)
                if linter_class == LAST_TOGGLED_LINTER_CLASS
            )
        except StopIteration:
            selected = -1

        def on_done(result):
            global LAST_TOGGLED_LINTER_CLASS

            if result == -1:
                return  # Canceled

            disable, linter_class, _ = linters[result]

            linter_class.disabled = disable
            LAST_TOGGLED_LINTER_CLASS = linter_class
            sublime.run_command('sublime_linter_config_changed')

            self.window.status_message(
                '{} {}.'.format(linter_class.name,
                                'disabled' if disable else 'enabled'))

        self.window.show_quick_panel(items, on_done, 0, selected)


def collect_possible_linters(view):
    rv = []
    for name, linter_class in persist.linter_classes.items():
        settings = linter.get_linter_settings(linter_class, view)

        could_lint_view = linter_class.matches_selector(view, settings)
        if not could_lint_view:
            continue

        if linter_class.disabled is not None:
            disabled = linter_class.disabled
        else:
            disabled = settings.get('disable')
        action = not disabled

        text = ('Enable: ' if disabled else 'Disable: ') + name
        rv.append((action, linter_class, text))

    return sorted(rv, key=lambda item: item[2])


class sublime_linter_addon_toggle_debug(sublime_plugin.WindowCommand):
    def run(self):
        current_mode = persist.settings.get('debug')
        next_mode = not current_mode

        self.window.status_message(
            "{} debug mode".format('Enabling' if next_mode else 'Disabling'))
        sublime.load_settings(
            "SublimeLinter.sublime-settings").set('debug', next_mode)


class sublime_linter_addon_choose_lint_mode(sublime_plugin.WindowCommand):
    def run(self, lint_mode=None):
        if lint_mode not in ('background', 'load_save', 'manual', 'save'):
            self.window.status_message(
                "'{}' is not a valid lint_mode".format(lint_mode))
            return

        current_mode = persist.settings.get('lint_mode')
        if lint_mode == current_mode:
            self.window.status_message(
                "Already in '{}' mode".format(lint_mode))
            return

        sublime.load_settings(
            "SublimeLinter.sublime-settings").set('lint_mode', lint_mode)

    def input(self, args):
        if 'lint_mode' in args:
            return None

        return LintModeInputHandler()


class LintModeInputHandler(sublime_plugin.ListInputHandler):
    def list_items(self):
        current_mode = persist.settings.get('lint_mode')
        all_modes = ['background', 'load_save', 'manual', 'save']

        try:
            selected = all_modes.index(current_mode)
        except ValueError:
            selected = 0

        return (all_modes, selected)
