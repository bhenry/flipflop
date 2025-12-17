(ns practice)

(def input (slurp "input.txt"))
(def lines (clojure.string/split-lines input))

(defn valid? [line]
  (let [[range* char* pw] (clojure.string/split line #" ")
        [low high] (clojure.string/split range* #"-")
        char-count (count (filter #(= % (first char*)) pw))]
    (when (<= (Integer. low) char-count (Integer. high))
      [range* (first char*) pw low high])))

(print (keep valid? lines))
(print (count (keep valid? lines)))
