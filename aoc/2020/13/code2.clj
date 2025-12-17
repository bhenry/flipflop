(ns thirteen)

(def input "7,13,x,x,59,x,31,19")
(def input "17,x,13,19")
(def input "67,7,59,61")
(def input "67,x,7,59,61")
(def input "67,7,x,59,61")
(def input "1789,37,47,1889")

(def input
 "13,x,x,41,x,x,x,x,x,x,x,x,x,467,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,353,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23")

(defn abs [i]
  (if (> 0 i)
    (* -1 i)
    i))

(defn gcd "(gcd a b) returns the greatest common divisor of a and b" [a b]
  (if (or (not (integer? a)) (not (integer? b)))
    (throw (IllegalArgumentException. "gcd requires two integers"))
    (loop [a (abs a) b (abs b)]
      (if (zero? b) a,
	  (recur b (mod a b))))))

(defn lcm*
  "(lcm a b) returns the least common multiple of a and b"
  [a b]
  (when (or (not (integer? a)) (not (integer? b)))
    (throw (IllegalArgumentException. "lcm requires two integers")))
  (cond (zero? a) 0
        (zero? b) 0
        :else (abs (* b (quot a (gcd a b))))))

(defn lcm [xs]
  (reduce lcm* (first xs) (rest xs)))

(defn bint [n]
  (bigint (Integer. n)))

(def requirements
  (map (fn [[a b]] [a (bint b)])
       (remove #(= (second %) "x")
               (map-indexed #(vector %1 %2) (clojure.string/split input #",")))))

(defn meets? [ts reqs]
  (every?
    (fn [[i b]]
      (= 0 (mod (+ ts i) b)))
    reqs))

(def found-ts
  (loop [ts 0
        incr (- (second (first requirements)) (first (first requirements)))
        found 1]
    (let [known-reqs (take found requirements)
          target-reqs (take (inc found) requirements)]
      (if (meets? ts requirements)
        ts
        (if (meets? ts target-reqs)
          (let [new-incr (lcm (map second target-reqs))]
            (recur (+ ts new-incr) new-incr (inc found)))
          (recur (+ ts incr) incr found))))))

(print found-ts)
