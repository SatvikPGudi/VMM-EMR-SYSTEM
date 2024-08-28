import json


class ParseTemplate:
    def __init__(self, template_file):
        with open(template_file, "r") as file:
            self.template = json.load(file)

    def parse_json_to_html(self, data, level=1):
        html_parts = []

        if isinstance(data, dict):
            fields = data.get("fields", [])
            for field in fields:
                label = field.get("label", "")
                field_id = field.get("id", "")
                field_type = field.get("type", "")
                input_type = field.get("inputType", "")
                placeholder = field.get("placeholder", "")

                if field_type == "group":
                    # Header tags based on level
                    html_parts.append(f'<div id="{field_id}" class="p-4">')
                    html_parts.append(f"<h{level}>{label}</h{level}>")
                    # Recursively process nested fields
                    html_parts.append(self.parse_json_to_html(field, level + 1))
                    html_parts.append("</div>")

                else:
                    html_parts.append('<div class=input-group mb-3">')
                    html_parts.append(
                        f'<span class="input-group-text">{label}</span>'
                    )
                    html_parts.append(
                        f'<{input_type} id="{field_id}" name="{field_id}" type="{field_type}" class="form-control" aria-label="{label}" placeholder="{placeholder}"></{input_type}>'
                    )
                    html_parts.append("</div>")
                    html_parts.append("<br>")

        return "\n".join(html_parts)

    def get_form(self):
        form_html = self.parse_json_to_html(self.template)
        form_html = (
            '<form action="/api/submit" method="post">'
            + form_html
            + '<button type="submit" class="btn btn-primary">Submit</button>'
            + "</form>"
        )

        return form_html
