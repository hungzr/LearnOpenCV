import  cv2


class Camera:
    def __init__(self, cam_num):
        self.cam_num = cam_num
        self.cap = None

    def initialize(self):
        self.cap = cv2.VideoCapture(self.cam_num)

    def get_frame(self):
        pass

    def acquire_movie(self, num_frames):
        pass

    def set_brightness(self, value):
        pass

    def __str__(self):
        return 'OpenCV Camera {}'.format(self.cam_num)

    def close_camera(self):
        self.cap.release()

if __name__ == '__main__':
    cam = Camera(0)
    cam.initialize()
    print(cam)
    cam.close_camera()