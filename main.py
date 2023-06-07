import cv2
import datetime


def main():

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=10, minSize=(10, 10))
        ppl.append(str(datetime.datetime.now()))
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('Face Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()


def write_to_file(ppl_list):

    with open("seen.txt", 'w') as file:

        print("-" * 10 + "Last Faces Seen" + '-' * 10)

        for date in ppl_list:
            file.write(date)
            file.write("\n")
            print("[+]" + date + "[+]")


if __name__ == '__main__':
    ppl = []

    main()
    write_to_file(ppl)

    print("\nDates saved to seen.txt")
