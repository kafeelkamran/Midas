#Import dependencies
import cv2
import torch
import matplotlib.pyplot as plt

#Download the MiDaS model
midas = torch.hub.load("intel-isl/MiDaS", "MiDaS")
midas.to('cpu')
midas.eval()

#Input tranformational pipeline
transformers = torch.hub.load("intel-isl/MiDaS", "transforms")
transformer = transformers.small_transform

#Hook into OpenCV
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Ignoring empty camera frame.")
        continue
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    input_batch = transformer(frame).unsqueeze(0)
    with torch.no_grad():
        prediction = midas(input_batch)
    prediction = torch.nn.functional.interpolate(
        prediction.unsqueeze(1),
        size=frame.shape[:2],
        mode="bicubic",
        align_corners=False,
    ).squeeze()
    output = prediction.cpu().numpy()
    plt.imshow(output)
    plt.show()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break