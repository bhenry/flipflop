(ns practice)

(def input (slurp "input.txt"))
(def lines (clojure.string/split-lines input))

(defn valid? [line]
  (let [[range* char* pw] (clojure.string/split line #" ")
        [low high] (clojure.string/split range* #"-")
        char-at-low (get pw (dec (Integer. low)))
        char-at-high (get pw (dec (Integer. high)))
        pos1 (= char-at-low (first char*))
        pos2 (= char-at-high (first char*))]
    (when (or (and pos1 (not pos2))
              (and pos2 (not pos1)))
      true)))

(print (keep valid? lines))
(print (count (keep valid? lines)))
