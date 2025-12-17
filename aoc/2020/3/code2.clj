(ns trees)

(def land (slurp "trees.txt"))
(def lanes (clojure.string/split-lines land))

(def tree_count (atom 0))

(doseq [[i row] (map-indexed vector lanes)]
  (when (and (= 0 (mod i 2))
             (= \# (get row (mod (* i 0.5) (count row)))))
    (swap! tree_count inc)))

; Right 1, down 1. - 90
; Right 3, down 1. - 244
; Right 5, down 1. - 97
; Right 7, down 1. - 92
; Right 1, down 2. - 48

(print (* 90 244 97 92 48))
