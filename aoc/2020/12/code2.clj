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
(def wx (atom 10))
(def wy (atom 1))
(def directions [\E \S \W \N])
(def direction (atom 0))

(defn pivot [dir]
  (let [[bx by] [@x @y]
        [wx1 wy1] [@wx @wy]]
    (cond
      (= dir \R)
      (do
        (if (> wx1 bx)
          (reset! wy (- by (- wx1 bx)))
          (reset! wy (+ by (- bx wx1))))
        (if (> wy1 by)
          (reset! wx (+ bx (- wy1 by)))
          (reset! wx (- bx (- by wy1)))))
      (= dir \L)
      (do
        (if (> wx1 bx)
          (reset! wy (+ by (- wx1 bx)))
          (reset! wy (- by (- bx wx1))))
        (if (> wy1 by)
          (reset! wx (- bx (- wy1 by)))
          (reset! wx (+ bx (- by wy1))))))))

(defn movewayward [dir dist]
  (condp = dir
    \N (swap! wy #(+ % dist))
    \S (swap! wy #(- % dist))
    \E (swap! wx #(+ % dist))
    \W (swap! wx #(- % dist))))

(defn towayward []
  (let [[bx by] [@x @y]
        [wx1 wy1] [@wx @wy]]
    (reset! x wx1)
    (reset! y wy1)
    (reset! wx (+ wx1 (- wx1 bx)))
    (reset! wy (+ wy1 (- wy1 by)))
    ))

(defn move [i]
  (let [inst (first i)
        dist (Integer. (apply str (rest i)))]
    (println [@x @y] [@wx @wy] i)
    (cond
      (#{\L \R} inst)
      (dotimes [_ (/ dist 90)]
        (pivot inst))
      (#{\N \S \E \W} inst)
      (movewayward inst dist)
      (= \F inst)
      (dotimes [_ dist]
        (towayward)))))

(doseq [i instructions]
  (move i))

(println [@x @y])
