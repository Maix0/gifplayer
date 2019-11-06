import tkinter
class Animation:
        def __init__(self,path="frames/frame_{}.gif", frame_min=0, frame_max=39,frame_interval=130):
            #======
            #ANIMATION SETUP
            self.coords = (0,0)
            self.frame_interval = frame_interval
            self.path = path
            self.frame_count= 0
            self.frames_limit= (frame_min,frame_max)
            self.frame_list = []
            self.load()
        def load(self):
            last_frame = None
            for i in range(self.frames_limit[0], self.frames_limit[1] + 1):
                try:
                    self.frame_list.append(tkinter.PhotoImage(file=self.path.format(i)))
                    last_frame = self.frame_list[-1]
                except:
                    if last_frame != None:
                        self.frame_list.append(last_frame)
                    raise "ERROR WTF"
        def next_frame(self) -> tkinter.PhotoImage:
            self.frame_count += 1
            if self.frame_count > self.frames_limit[1]:
                self.frame_count = self.frames_limit[0]
            return self.frame_list[self.frame_count]

class Rickroll:
    def __init__(self):
        self.master = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.master,width=320,height=240)
        self.anim = Animation()
        self.counter = 0
        self.frame_cache = None
        self.tick()
        self.canvas.pack(expand=True,fill="both")
        self.master.mainloop()

    def tick(self):
        #global canvas, anim,counter,frame_cache
        new_frame = self.anim.next_frame()
        self.canvas.delete(self.frame_cache)
        try:
            self.canvas.create_image(self.anim.coords[0],self.anim.coords[1], image=new_frame)
        except:
            print("excepted err in create image")
        self.canvas.coords(new_frame,self.anim.coords)
        print(self.counter, new_frame)
        self.counter += 1
        self.frame_cache = new_frame
        self.canvas.after(self.anim.frame_interval,self.tick)


Rickroll()
