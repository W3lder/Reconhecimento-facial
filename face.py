# Vamos importar uma biblioteca OpenCV pelo terminal "pip install opencv-python" Carregar o modelo Haar Cascade.
# Haar Cascade é um modelo treinado para reconhecer faces.
import cv2 
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Código para acessar a câmera do dispositivo
video_capture = cv2.VideoCapture(0)

# Função para detectar rostos no stream de vide e desenhar uma caixa delimitadora ao redor deles:
def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40,40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces

while True:
    result, video_frame = video_capture.read()
    if result is False:
        break # se i frane di vudei bão for lido com sucesso ele encerra o loop de leitura

    faces = detect_bounding_box(
        video_frame
    ) # Aplica a função do que criamos para os frame

    cv2.imshow(
        "Meu projeto de detcção de face!", video_frame
    ) # Vai exibir o quadro processado em uma janela chamada "Meu projeto de detcção de face!"

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()