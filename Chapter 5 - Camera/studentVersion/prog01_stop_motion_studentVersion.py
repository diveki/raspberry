# importald a cv2, time es subprocess csomagokat

cap = # inicializald a kamerat a cv2 csomag VideoCapture(0) metodusaval
nframe = 0

while True:
    ret, frame = # olvasd ki a kepet a cap objektum read metodusaval
    # jelenitsd meg a kepet a cv2 csomag imshow metodusaval: elso parameter egy sztring ami az abra neve, a masodik pedig a megjelenitendo kep, frame
    
    if cv2.waitKey(100) & 0xFF == ord('p'):
        nframe = # noveld az nframe erteket 1-gyel
        print(f'snaphot {nframe:03d} done!')
        # a cv2 csomag imwrite metodusat hasznalva mentsd el jpg formaban a keszitett kepet, hogy pl. frame001.jpg legyen a neve, ahol az nframe erteke jelenti a frame utani szamot. A masodik parameter a metodusban maga a kep, frame. 
    
    if cv2.waitKey(100) & 0xFF == ord('q'):
        # ha a q billentyut lenyomjak, lepj ki a vegtelen while ciklusbol
    # a time csomagbol a sleep fugvennyel varakoztass 0.2 masodpercet

cap.release()
# Bezarunk minden ablakot, amit a program megnyitott
cv2.destroyAllWindows()

subprocess.call('ffmpeg -r 1 -i animation/frame%03d.jpg -qscale 1 animation.mp4')
