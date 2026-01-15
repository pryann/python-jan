def generate_new_id(items):
    max_id = 0
    for item in items:
        if item["id"] > max_id:
            max_id = item["id"]
    return max_id + 1


def get_items(items):
    return items


def find_item_by_id(item_id, items):
    for item in items:
        if item["id"] == item_id:
            return item


def create_item(item_payload, items):
    new_item = {"id": generate_new_id(items)}
    new_item.update(item_payload)
    items.append(new_item)
    return items[-1]


def update_item(item_id, item_payload, items):
    item = find_item_by_id(item_id, items)
    if item is not None:
        index = items.index(item)
        items[index].update(item_payload)
        return items[index]


def remove_item(item_id, items):
    item = find_item_by_id(item_id, items)
    if item is not None:
        items.remove(item)
    return item
