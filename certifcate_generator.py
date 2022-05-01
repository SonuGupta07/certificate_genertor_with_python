import cv2

list_of_names = []


def copy_data():
    with open("namelist.txt")as file:
        for line in file:
            list_of_names.append(line.strip())


copy_data()


def generate_certificate():
    for name in list_of_names:
        template = cv2.imread("certificate_template.jpg")
        cv2.putText(template, name, (770, 980),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5, cv2.LINE_AA)
        cv2.imwrite(f'generated_certificate/{name}.jpg', template)


generate_certificate()
