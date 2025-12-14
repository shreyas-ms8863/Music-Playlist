from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Doubly Linked List Node
class Node:
    def __init__(self, song):
        self.song = song
        self.prev = None
        self.next = None

# Playlist using Doubly Linked List
class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_song(self, song):
        new_node = Node(song)
        if not self.head:
            self.head = self.tail = self.current = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def next_song(self):
        if self.current and self.current.next:
            self.current = self.current.next

    def prev_song(self):
        if self.current and self.current.prev:
            self.current = self.current.prev

playlist = Playlist()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        song = request.form.get("song")
        if song:
            playlist.add_song(song)
        return redirect(url_for("index"))

    current_song = playlist.current.song if playlist.current else "No song in playlist"
    return render_template("index.html", current_song=current_song)

@app.route("/next")
def next():
    playlist.next_song()
    return redirect(url_for("index"))

@app.route("/prev")
def prev():
    playlist.prev_song()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
