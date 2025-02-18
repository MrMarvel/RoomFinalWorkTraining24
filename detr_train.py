import torch

model = torch.hub.load('facebookresearch/detr:main', 'detr_resnet50', pretrained=True)
import cv2
import torch
import supervision as sv


#
#
# with torch.no_grad():
#
#     # load image and predict
#     image = cv2.imread(IMAGE_PATH)
#     inputs = image_processor(images=image, return_tensors='pt').to(DEVICE)
#     outputs = model(**inputs)
#
#     # post-process
#     target_sizes = torch.tensor([image.shape[:2]]).to(DEVICE)
#     results = image_processor.post_process_object_detection(
#         outputs=outputs,
#         threshold=CONFIDENCE_TRESHOLD,
#         target_sizes=target_sizes
#     )[0]
#
# # annotate
# detections = sv.Detections.from_transformers(transformers_results=results).with_nms(threshold=IOU_TRESHOLD)
#
# labels = [
#     f"{model.config.id2label[class_id]} {confidence:0.2f}"
#     for _, confidence, class_id, _
#     in detections
# ]
#
# box_annotator = sv.BoxAnnotator()
# frame = box_annotator.annotate(scene=image, detections=detections, labels=labels)
#
# %matplotlib inline
# sv.show_frame_in_notebook(frame, (16, 16))