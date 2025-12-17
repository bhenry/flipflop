(ns chargers
  (:require [clojure.string :as str]))

(def data (slurp "input.txt"))
(def adapters
  (->> (str/split-lines data)
       (map #(Integer. %))
       (sort)))

(println adapters)

(def count1 (atom 0))
(def count3 (atom 0))

(defn doit [input]
  (reset! count1 0)
  (reset! count3 0)
  (println (partition 2 1 (sort (cons 0 input))))
  (doseq [[a b] (partition 2 1 (sort (cons 0 input)))]
    (cond
      (= 1 (- b a)) (swap! count1 inc)
      (= 3 (- b a)) (swap! count3 inc))))

(def input [
  16
  10
  15
  5
  1
  11
  7
  19
  6
  12
  4
])

(doit adapters)
(println (* @count1 (inc @count3)))
