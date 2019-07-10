import tempfile
import random
import re
from faker import Faker


class HTML_CREATOR:
    def __init__(self):
        self.faker = Faker()

    def get_table_html(self, num_cols, num_rows, bold_word_id=1, bold_block_id=1,):
        table_header_bgcolors = ["#dddddd", "#ddffdd",
                                 "#ffffdd", "#ddffff", "#ffffff"]
        background_colors = ["#dddddd", "#ddffdd",
                             "#ffffdd", "#ddffff", "#ffffff"]
        font_family = ["arial, sans-serif"]
        alignment = ["center", "left", "right", "center"]
        html_content = list()
        tagged_ids = list()
        bold_tag_name = None

        # html barebone
        html_content.append("<!DOCTYPE html>\n")
        html_content.append("<html>\n")
        html_content.append("<head>\n")
        html_content.append("<style>\n")
        html_content.append(
            f"table {{font-family: {random.choice(font_family)}; border-collapse: collapse; width: {random.choice(range(80, 101))}%;}}\n")
        html_content.append(
            f"th {{border: {random.choice(range(1,4))}px solid #dddddd;background-color: {random.choice(table_header_bgcolors)};text-align: {random.choice(alignment)};padding: {random.choice(range(6, 17))}px;}}\n")
        html_content.append(
            f"td {{border: {random.choice(range(1,2))}px solid #dddddd;background-color: {random.choice(background_colors)};text-align: {random.choice(alignment)};padding: {random.choice(range(6, 17))}px;}}\n")
        html_content.append(
            f".after-table {{text-align: {random.choice(alignment)};}}\n")
        if random.choice([True, False]):
            html_content.append(
                f"tr:nth-child(even) {{background-color: {random.choice(background_colors)};}}\n")
        html_content.append("</style>\n")
        html_content.append("</head>\n")
        html_content.append("<body>\n")
        # html barebone

        column_names = [self.faker.domain_word().capitalize()
                        for _ in range(num_cols)]

        html_content.append("<center><table>\n")
        # random caption around table
        if random.choice([True, False, True]):
            if random.choice([True, False, True]):
                bold_tag_name = f"bold_block_{bold_block_id}"
                html_content.append("<caption>\n<b id='{1}'>{0}</b>\n</caption>\n".format(
                    "<br>".join([i.strip('.') for i in self.faker.sentences(3)]), bold_tag_name))
                tagged_ids.append(bold_tag_name)
                bold_block_id += 1
            elif random.choice([True, False, False]):
                bold_tag_name = f"bold_word_{bold_word_id}"
                caption_entry = [i.strip('.') for i in self.faker.sentences(3)]
                random_bold_word = random.choice(
                    [i for i in " ".join(caption_entry).split() if len(i) > 5])
                caption_entry = [i.replace(
                    random_bold_word, f"<b id='{bold_tag_name}'>{random_bold_word}</b>") for i in caption_entry]
                caption_entry = "<br>".join(caption_entry)
                html_content.append(
                    f"<caption>\n{caption_entry}\n</caption>\n")
                tagged_ids.append(bold_tag_name)
                bold_word_id += 1
            else:
                html_content.append("<caption>\n{}\n</caption>\n".format(
                    "<br>".join([i.strip('.') for i in self.faker.sentences(3)])))

        # random caption around table
        html_content.append(f"<tr>\n")

        for column in column_names:
            bold_tag_name = f"bold_word_{bold_word_id}"
            html_content.append(
                f"<th>\n<b id='{bold_tag_name}'>{column}</b></th>\n")
            tagged_ids.append(bold_tag_name)
            bold_word_id += 1
        html_content.append("</tr>\n")

        for _ in range(num_rows):
            html_content.append("<tr>\n")
            for col in range(num_cols):
                if random.random() > 0.95:
                    bold_tag_name = f"bold_word_{bold_word_id}"
                    col_data = self.faker.sentence().strip('.')
                    eligible_words = [
                        i for i in col_data.split() if len(i) > 4]
                    if not len(eligible_words):
                        continue
                    random_bold_word = random.choice(eligible_words)
                    col_data = col_data.replace(
                        random_bold_word, f"<b id='{bold_tag_name}'>{random_bold_word}</b>")
                    html_content.append(f"<td>\n{col_data}</td>\n")
                    tagged_ids.append(bold_tag_name)
                    bold_word_id += 1
                else:
                    html_content.append(
                        f"<td>\n{self.faker.sentence().strip('.')}</td>\n")
            html_content.append("</tr>\n")

        html_content.append("</table></center>\n")

        # random para around table
        if random.choice([True, False]):
            if random.choice([True, False]):
                bold_tag_name = f"bold_word_{bold_word_id}"
                after_table_entry = [i.strip('.')
                                     for i in self.faker.sentences(6)]
                random_bold_word = random.choice(
                    [i for i in " ".join(after_table_entry).split() if len(i) > 5])
                after_table_entry = [i.replace(
                    random_bold_word, f"<b id='{bold_tag_name}'>{random_bold_word}</b>") for i in after_table_entry]
                after_table_entry = "<br>".join(after_table_entry)
                html_content.append(
                    f"<p class='after-table'>\n{after_table_entry}\n</p>\n")
                tagged_ids.append(bold_tag_name)
                bold_word_id += 1
            else:
                html_content.append(
                    "<p class='after-table'>\n{}</p>\n".format("<br>".join(self.faker.sentences(6))))
        # random para around table

        # html barebone
        html_content.append("</body>\n")
        html_content.append("</html>\n")
        # html barebone
        return html_content, tagged_ids

    def get_html(self):
        html_content = list()

        # html barebone
        html_content.append("<!DOCTYPE html>\n")
        html_content.append("<html>\n")
        html_content.append("<body>\n")
        # html barebone

        # html barebone
        html_content.append("</body>\n")
        html_content.append("</html>\n")
        # html barebone
        return html_content
