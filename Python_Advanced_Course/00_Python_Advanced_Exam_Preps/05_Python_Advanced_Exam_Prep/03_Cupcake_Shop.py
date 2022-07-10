def stock_availability(list_of_boxes, delivery_or_sell, *args):
    current_list_of_boxes = list_of_boxes

    if delivery_or_sell == "delivery":
        new_boxes = args
        current_list_of_boxes.extend(new_boxes)
    elif delivery_or_sell == "sell":
        if not args:
            current_list_of_boxes = current_list_of_boxes[1:]
        elif len(args) == 1 and str(*args).isdigit():
            boxes_sold = int(str(*args))
            current_list_of_boxes = current_list_of_boxes[boxes_sold:]
        else:
            box_types = list(args)
            for box in box_types:
                while box in current_list_of_boxes:
                    current_list_of_boxes.remove(box)

    return current_list_of_boxes
