def drawIntroScene(canvas,data):
    if data.introMode == True:
        # draw background
        canvas.create_rectangle(0, 0, data.width, data.height, fill="gold")
        # draw start button
        canvas.create_rectangle((0.5 * data.width - 200), (0.5 * data.height - 150), (0.5 * data.width + 200),
                                (0.5 * data.height + 150), fill="white")
        canvas.create_text(data.width, 0.5 * data.height, anchor="e", fill="brown",
                           font="Arial 30 bold", text="Intro Page")
def displayHearMsg(canvas,data):
    # this function is used to display message only for 2 seconds
    canvas.create_text(data.width, 0.8 * data.height, anchor="e", fill="brown",
                       font="Arial 30 bold", text=data.hearMessage)
    canvas.after(2000,displayEmptyMsg(canvas,data))

def displayEmptyMsg(canvas,data):
    print("now go away")
    canvas.create_text(data.width, 0.8 * data.height, anchor="e", fill="brown",
                       font="Arial 30 bold", text="")

def drawSpeakScene(canvas,data):
    if data.speakMode == True:
        canvas.create_rectangle(0, 0, data.width, data.height, fill="lightblue")
        for bubble in data.bubbles:
            print("bubble",bubble)
            bubble.draw(canvas)
        canvas.create_text(data.width / 2, data.height, anchor="s", fill="yellow",
                           font="Arial 24 bold", text="Score: " + str(data.score))
        displayHearMsg(canvas,data)
        canvas.create_text(data.width, 0.5 * data.height, anchor="e", fill="brown",
                           font="Arial 30 bold", text=data.speakingInstruction)
        # draw Next button
        canvas.create_rectangle(data.nextx1, data.nexty1, data.nextx2, data.nexty2, fill = "green")

def drawSortScene(canvas,data):
    pass

def redrawAll(canvas,data):
    drawIntroScene(canvas,data)
    drawSpeakScene(canvas,data)
    drawSortScene(canvas,data)