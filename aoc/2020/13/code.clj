(ns thirteen)

(def ts 939)
(def input "7,13,x,x,59,x,31,19")

(def ts 1008713)
(def input
"13,x,x,41,x,x,x,x,x,x,x,x,x,467,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,353,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23")


(def buses (map #(Integer. %) (filter #(not (= "x" %)) (clojure.string/split input #","))))

(println buses)

(def bestwait (atom 100000000000))
(def bestbus (atom nil))

(doseq [b buses]
  (let [tobus (inc (quot ts b))
        wait (- (* tobus b) ts)]
    (when (> @bestwait wait)
      (reset! bestwait wait)
      (reset! bestbus b))))
(print (* @bestwait @bestbus))
