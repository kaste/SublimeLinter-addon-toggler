import sublime
import sublime_plugin

from SublimeLinter.lint import persist, linter


class sublime_linter_addon_toggle_linters(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        linters = collect_possible_linters(view)
        if not linters:
            self.window.status_message(
                'No possible linters registered for this view. :-(')
            return

        items = [text for _, _, text in linters]

        def on_done(result):
            if result == -1:
                return  # Canceled

            disable, linter_class, _ = linters[result]

            linter_class.disabled = disable
            sublime.run_command('sublime_linter_config_changed')

            self.window.status_message(
                '{} {}.'.format(linter_class.name,
                                'disabled' if disable else 'enabled'))

        self.window.show_quick_panel(items, on_done)


def collect_possible_linters(view):
    rv = []
    for name, linter_class in persist.linter_classes.items():
        settings = linter.get_linter_settings(linter_class, view)

        could_lint_view = linter_class.matches_selector(view, settings)
        if not could_lint_view:
            continue

        disabled = linter_class.disabled or settings.get('disable')
        action = not disabled

        text = ('Enable: ' if disabled else 'Disable: ') + name
        rv.append((action, linter_class, text))

    return sorted(rv, key=lambda item: item[2])
