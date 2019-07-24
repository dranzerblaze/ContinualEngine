import cv2

def check_horizontal_bbox_overlap(a,b):
    a_xmin , a_xmax = a[0] , a[2] 
    b_xmin , b_xmax = b[0] , b[2] 
    bias = 5
    a_xmin_range = range(a_xmin - bias , a_xmin + bias)
    a_xmax_range = range(a_xmax - bias , a_xmax + bias)
    b_xmin_range = range(b_xmin - bias , b_xmin + bias)
    b_xmax_range = range(b_xmax - bias , b_xmax + bias)
    flag =  False
    flag_1 = False
    flag_2 = False
    a_xmin_set = set(a_xmin_range)
    b_xmin_set = set(b_xmin_range)
    if(len(a_xmin_set.intersection(b_xmax_range)) > 0):
        flag_1 = True
    if (len(b_xmin_set.intersection(a_xmax_range)) > 0):
        flag_2 = True
    if ( flag_1 == True or flag_2 == True):
        return True
    return False


def join_bbox(a,b):
    a_xmin , a_ymin , a_xmax , a_ymax = a[0] ,a[1] ,a[2] , a[3]
    b_xmin , b_ymin , b_xmax , b_ymax = b[0] , b[1] , b[2] ,b[3]
    ans_xmin = min(a_xmin , b_xmin)
    ans_xmax = max(a_xmax , b_xmax)
    ans_ymin = min(a_ymin , b_ymin)
    ans_ymax = max(a_ymax , b_ymax)
    return (ans_xmin,ans_ymin,ans_xmax,ans_ymax)

for i in range(1,8):
    filename = str(i) + ".png"
    image= cv2.imread(filename)
    gray= cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
    _ , thresh = cv2.threshold(gray , 155, 255 , cv2.THRESH_BINARY_INV)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
    dilated = cv2.dilate(thresh , kernel , iterations = 14)
    contours , hierarchy = cv2.findContours(dilated , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
    border_px = 6
    bbox_list = []
    for contour in contours:
        [x,y,w,h] = cv2.boundingRect(contour)
        if (h>700 and w>700):
            continue
        elif(h<30 and w<30):
            continue
        cv2.rectangle(image , (x + border_px,y + border_px) , (x+w - border_px,y+h - border_px) , (255,0,255) , 1)
    output_new = "countoured_new" + str(i) + ".png"
    cv2.imwrite(output_new , image)
    # bbox_updated = []
    # bbox_to_be_removed = []
    # for j in range(len(bbox_list)-1):
    #     for k in range(i+1 , len(bbox_list)):
    #         if(check_horizontal_bbox_overlap(bbox_list[j] , bbox_list[k]) == True):
    #             result_bbox = join_bbox(bbox_list[j] , bbox_list[k])
    #             bbox_updated.append(result_bbox)
    #             bbox_to_be_removed.append(bbox_list[j])
    #             bbox_to_be_removed.append(bbox_list[k])
    # print (len(bbox_updated) , "update")
    # print (len(bbox_to_be_removed) , "remove")
    # bbox_removed = []
    # for bbox in bbox_to_be_removed:
    #     if(bbox_removed.count(bbox) == 0):
    #         bbox_list.remove(bbox)
    #         bbox_removed.append(bbox)
    # for bbox in bbox_updated:
    #     bbox_list.append(bbox)
    # for bbox in bbox_list:
    #     cv2.rectangle(image, (bbox[0] , bbox[1]),(bbox[2],bbox[3]),(255,0,255),1)
    # output_new = "countoured_new" + str(i) + ".png"
    # cv2.imwrite(output_new , image)

