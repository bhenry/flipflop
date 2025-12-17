(ns twelve
  (:require [clojure.string :as str]))

(def input "F10
N3
F7
R90
F11")

(def input (slurp "input.txt"))

(def instructions (->
  input
  str/split-lines))

(println instructions)

(def x (atom 0))
(def y (atom 0))
(def directions [\E \S \W \N])
(def direction (atom 0))

(defn pivot [dir]
  (cond
    (= dir \R)
    (swap! direction #(mod (inc %) 4))
    (= dir \L)
    (swap! direction #(if (= 0 %) 3 (dec %)))))

(defn travel [dir dist]
  (condp = dir
    \N (swap! y #(+ % dist))
    \S (swap! y #(- % dist))
    \E (swap! x #(+ % dist))
    \W (swap! x #(- % dist))))

(defn move [i]
  (let [inst (first i)
        dist (Integer. (apply str (rest i)))]
    (cond
      (#{\L \R} inst)
      (dotimes [x (/ dist 90)]
        (pivot inst))
      (#{\N \S \E \W} inst)
      (travel inst dist)
      (= \F inst)
      (travel (get directions @direction) dist))))

(doseq [i instructions]
  (move i))

(println [@x @y])
