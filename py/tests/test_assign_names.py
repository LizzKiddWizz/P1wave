import unittest
from h2o_wave import ui
from utils.assign_names import assign_names


class TestAssignNames(unittest.TestCase):

    def test_form_card_items(self):
        # form card with unnamed items
        card = ui.form_card(box='1 1 1 1', items=[
            ui.text_xl(content='Hello'),
            ui.button(label='Click Me'),
            ui.textbox(name='already_named', label='Named Box'),
        ])
        page = {'form': card}

        assign_names(page)

        item_names = [item.name for item in card.items]
        self.assertIn('auto_item_1', item_names)
        self.assertIn('auto_item_2', item_names)
        self.assertIn('already_named', item_names)

    def test_buttons_group(self):
        buttons = ui.buttons([
            ui.button(label='One'),
            ui.button(name='two', label='Two'),
        ])
        assign_names(buttons)

        button_names = [btn.name for btn in buttons.items]
        self.assertIn('auto_item_1', button_names)
        self.assertIn('two', button_names)

    def test_notification_bar_buttons(self):
        bar = ui.notification_bar(text='Info', buttons=[
            ui.button(label='Dismiss'),
        ])
        assign_names(bar)

        button_names = [btn.name for btn in bar.buttons]
        self.assertIn('auto_item_1', button_names)

    def test_dialog_items(self):
        dialog = ui.dialog(title='My Dialog', items=[
            ui.text(content='Dialog text'),
            ui.button(label='Submit'),
        ])
        assign_names(dialog)

        item_names = [item.name for item in dialog.items]
        self.assertIn('auto_item_1', item_names)
        self.assertIn('auto_item_2', item_names)

    def test_side_panel_items(self):
        panel = ui.side_panel(title='Side', items=[
            ui.text(content='Side content'),
        ])
        assign_names(panel)

        item_names = [item.name for item in panel.items]
        self.assertIn('auto_item_1', item_names)
if name == 'main':
    unittest.main()