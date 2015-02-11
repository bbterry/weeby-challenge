package main

import (
	"fmt"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Access-Control-Allow-Origin", "*")
	fmt.Fprint(w, "hello, world")
}

func main() {
	http.HandleFunc("/weeby/magic", handler)
	fmt.Println("listening at http://0.0.0.0:1337")
	http.ListenAndServe(":1337", nil)
}
