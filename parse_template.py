import json

def load_json(filename: str) -> dict:
    with open(filename, "r") as file:
        template = json.load(file)

    return template


def parse_json_to_html(data, level=1):
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
                html_parts.append(parse_json_to_html(field, level + 1))
                html_parts.append("</div>")
                html_parts.append("<hr>")

            else:
                if input_type == "textarea":
                    html_parts.append('<div class=input-group mb-3">')
                    html_parts.append(f'<span class="input-group-text">{label}</span>')
                    html_parts.append(
                        f'<textarea id="{field_id}" class="form-control" aria-label="{label}" placeholder="{placeholder}"></textarea>'
                    )
                    html_parts.append("</div>")
                    html_parts.append("<br>")

                elif input_type == "input":
                    html_parts.append('<div class=input-group mb-3">')
                    html_parts.append(f'<span class="input-group-text">{label}</span>')
                    html_parts.append(
                        f'<input type="{field_type}" id="{field_id}" class="form-control" aria-label="{label}" placeholder="{placeholder}">'
                    )
                    html_parts.append("</div>")
                    html_parts.append("<br>")

    return "\n".join(html_parts)


if __name__ == "__main__":
    template = load_json("template.json")
    html_output = parse_json_to_html(template)

    print(html_output)
