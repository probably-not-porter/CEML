import create_model as CM
import process_images as PI

print("CREATING BASE EDGE DETECTIONS")
PI.main("../../data/xray_parent/xray", True, True, True, True, True, True, True, True, False) # Create all images

print("CANNY AUTO + CANNY WIDE + CANNY TIGHT - IMAGE COMPOSITE")
out = PI.main("../../data/xray_parent/xray", True, True, True, False, False, False, False, False, True)

print("CANNY AUTO + CANNY WIDE + CANNY TIGHT - RESNET18 MODEL")
CM.main(out[-1], "resnet18", 10)

print("CANNY AUTO + CANNY WIDE + CANNY TIGHT - RESNET34 MODEL")
CM.main(out[-1], "resnet34", 10)

print("CANNY AUTO + CANNY WIDE + CANNY TIGHT - RESNET50 MODEL")
CM.main(out[-1], "resnet50", 10)