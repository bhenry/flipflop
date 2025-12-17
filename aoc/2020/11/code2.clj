(ns code
  (:require [clojure.string :as str]))

(def input (slurp "in.txt"))
; (def input (slurp "input.txt"))

(def grid (str/split-lines input))
(def seating (atom {}))

(doseq [y (range (count grid))]
  (doseq [x (range (count (get grid y)))]
    (swap! seating assoc [x y] (get (get grid y) x))))

(defn get-neighbors [p]
  ((apply juxt (for [a [-1 0 1]
                     b [-1 0 1]
                     :when (not= [0 0] [a b])]
                 (fn [[x y]] [(+ x a) (+ y b)]))) p))

(defn get-neighbors [p]
  (let [slopes [[1 1]
                [1 0]
                [1 -1]
                [0 -1]
                [-1 -1]
                [-1 0]
                [-1 1]
                [0 1]]
    ))

(defn count-neighbors [m p]
  (let [neighbors (map m (get-neighbors p))]
    (count (filter #(= \# %) neighbors))))

(defn change-seats []
  (let [seat-state @seating]
    (doseq [[p s] seat-state]
      (let [neighbors (count-neighbors seat-state p)]
        (cond (and (= s \L) (= 0 neighbors))
              (swap! seating assoc p \#)
              (and (= s \#) (< 3 neighbors))
              (swap! seating assoc p \L))))))

(defn print-seats []
  (doseq [[y r] (zipmap (range) grid)]
    (print "\n")
    (doseq [[x s] (zipmap (range) r)]
      (print (@seating [x y])))))

(println input)

(dotimes [n 125]
  (let [old @seating]
    (change-seats)
    ; (print-seats)
    ; (println "")
    (if (= old @seating)
      (println n))))

(println (count (filter #(= \# %) (vals @seating))))


; (println @seating)
