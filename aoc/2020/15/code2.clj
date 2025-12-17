(ns elves
)

(def input
[
; [0,3,6,436]
; [1,3,2,1]
; [2,1,3,10]
; [1,2,3,27]
; [2,3,1,78]
; [3,2,1,438]
; [3,1,2,1836]
[0,3,1,6,7,5, :ans]
]
)

(defn i [n]
  (Integer. n))

(def tracker (atom []))

(defn track [& args]
  (let [starters (butlast args)]
    (reset! tracker (into {} (map-indexed (fn [i n] [n (inc i)]) starters))))
    (print @tracker)
  (loop [turn (count args)
         recent (last args)]
    (let [used (get @tracker recent)
          new (if used
                (- turn used)
                0)]
      (swap! tracker assoc recent turn)
      (if (< turn 30000000)
        (recur (inc turn)
               new)
        (println args "30000000th" recent)))))

(doseq [t input]
  (apply track (butlast t)))
